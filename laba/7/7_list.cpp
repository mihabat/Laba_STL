#include<iostream>
#include<list>
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
    ofstream l;
    l.open("list.txt");
    list<int> listic;
    for(int i = 1; i <= 100000; i++)
    {
        double start_time = 0, end_time = 0;
        listic.push_back(-1000 + rand() % 2001);
        list<int>::iterator it_list = listic.begin();
        start_time = get_time();
        while(it_list != listic.end())
        {
            it_list++;
        }
        end_time = get_time();
        l << end_time - start_time << endl;
        cout<<i<<endl;
    }
}
