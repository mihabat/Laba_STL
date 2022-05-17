#include<iostream>
#include<map>
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
    ofstream m;
    m.open("map.txt");
    map<int, int>maP;
    for(int i = 1; i <= 100000; i++)
    {
        double start_time = 0, end_time = 0;
        maP[i] = -1000 + rand() % 2001;
        map<int, int>::iterator it_map = maP.begin();
        start_time = get_time();
        while(it_map != maP.end())
        {
            it_map++;
        }
        end_time = get_time();
        m << end_time - start_time << endl;
        cout<<i<<endl;
    }
}
