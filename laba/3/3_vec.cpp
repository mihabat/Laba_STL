#include<iostream>
#include<vector>
#include<ctime>
#include<cstdlib>
#include<chrono>
#include<fstream>
using namespace std;

double get_time()
{
    return std::chrono::duration_cast<std::chrono::microseconds>(std::chrono::steady_clock::now().time_since_epoch()).count();
}

int main()
{
    ofstream v;
    v.open("vector_erase.txt");
    for(int i = 1; i <= 100000; i++)
    {
        vector<int>vec;
        double start_time = 0, end_time = 0;
        for(int j = 0; j < i; j++)
        {
            vec.push_back(-1000 + rand() % 2001);
        }

        auto it = vec.cbegin();
        int index = rand() % i;
        start_time = get_time();
        vec.erase(it + index);
        end_time = get_time();
        v << end_time - start_time << endl;
        vec.clear();
        cout<<i<<endl;
    }
}
