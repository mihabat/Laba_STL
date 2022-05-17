#include<iostream>
#include<ctime>
#include<cstdlib>
#include<chrono>
#include<fstream>
#include<algorithm>
using namespace std;

template <typename T>
class subvector {
public:

    subvector(T a) { //инициализация пустого недовектора (top и capacity по нулям, а mas это NULL)
        this->mas = nullptr;
        this->top = 0;
        this->capacity = 0;
    }
    ~subvector() { //очистить всю используемую память, инициализировать недовектор как пустой
        if (this->capacity > 0) {
            delete []this->mas;
            this->mas = nullptr;
            this->top = 0;
            this->capacity = 0;
        }
    }

    bool resize(unsigned int new_capacity) { //увеличить емкость недовектора
    // (можно использовать и для уменьшения - тогда, в рамках данной реализации, если top меньше новой capacity,
    // то копируем только то, что влезает, и уменьшаем top до capacity)
        if (new_capacity != 0) {
            T *mas2 = new T[new_capacity];
            memcpy(mas2, this->mas, min(new_capacity, this->capacity) * sizeof(int));
            this->capacity = new_capacity;
            this->top = min(this->top, new_capacity);
            delete []this->mas;
            this->mas = mas2;
        }
        else {
            if (this->capacity > 0) {
                delete[]this->mas;
                this->mas = nullptr;
                this->top = 0;
                this->capacity = 0;
            }
        }
        return true;
    }

    void push_back(T d) {
    //добавление элемента в конец недовектора с выделением дополнительной памяти при необходимости
        if (this->capacity == 0) {
            resize(10);
        }
        else if (this->top >= this->capacity) {
            resize(this->capacity * 2);
        }
        *(this->mas + this->top) = d;
        this->top++;
    }

    int pop_back() { //удаление элемента с конца недовектора, значение удаленного элемента вернуть
        if (this->top > 0) {
            int res = *(this->mas + this->top - 1);
            this->top--;
            return res;
        }
        return 0;
    }

    void shrink_to_fit() { //очистить неиспользуемую память
        resize(this->top);
    }

    void clear() { //очистить содержимое недовектора, занимаемое место при этом не меняется
        memcpy(this->mas, 0, this->capacity * sizeof(int));
        this->top = 0;
    }

    void insert(T el, unsigned int i) {
        if (this->top == this->capacity) {
            resize(this->capacity * 2);
        }
        memcpy(this->mas + i + 1, this->mas + i, (this->top - i) * sizeof(T));
        this->top++;
        this->mas[i] = el;
    }

     int erase(unsigned int i) {
        if (i >= 0 && this-> top > i) {
            int res = *(this->mas + i);
            memcpy(this->mas + i, this->mas + i + 1, (this->top - i) * sizeof(T));
            this->top--;
            return res;
        }
        return 0;
     }

    T &operator[](const int& index) {
        if (index >= 0 && index < capacity)
            return *(mas + index);
        return *(mas);
    }

    class Iterator {
    private:
        T* p;
    public:
        Iterator (T* first) {
            p = first;
        }
        bool operator !=(const Iterator& it) const {
            return p != it.p;
        }
        bool operator ==(const Iterator& it) const {
            return p != it.p;
        }
        T& operator+(int n) {
            return *(p + n);
        }
        T& operator-(int n) {
            return *(p - n);
        }
        T& operator++() {
            return *(++p);
        }
        T& operator--() {
            return *(--p);
        }
        T& operator*() {
            return *p;
        }
    };
    Iterator begin() {
        return mas;
    }
    Iterator end() {
        return mas + top;
    }
    T *mas;
    unsigned int top;
    unsigned int capacity;
};
double get_time()
{
    return std::chrono::duration_cast<std::chrono::microseconds>(std::chrono::steady_clock::now().time_since_epoch()).count();
}
int main()
{
    ofstream v;
    v.open("subvector_erase.txt");
    for(int i = 1; i <= 100000; i++)
    {
        subvector Subv(1);
        double start_time = 0, end_time = 0;
        for(int j = 0; j < i; j++)
        {
            Subv.push_back(-1000 + rand() % 2001);
        }
        int index = rand() % i;
        start_time = get_time();
        Subv.erase(index);
        end_time = get_time();
        v << end_time - start_time << endl;
        cout<<i<<endl;
    }
}
