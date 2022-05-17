#include<iostream>
#include<forward_list>
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
    ofstream f_l;
    f_l.open("forward_list.txt");
    forward_list<int> forw_list;
    for(int i = 1; i <= 100000; i++)
    {
        double start_time = 0, end_time = 0;
        forw_list.push_front(-1000 + rand() % 2001);
        forward_list<int>::iterator it_fl = forw_list.begin();
        start_time = get_time();
        while(it_fl != forw_list.end())
        {
            it_fl++;
        }
        end_time = get_time();
        f_l << end_time - start_time << endl;
        cout<<i<<endl;
    }
}
