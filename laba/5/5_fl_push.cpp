#include<iostream>
#include<forward_list>
#include<ctime>
#include<cstdlib>
#include<chrono>
#include<fstream>
using namespace std;

double get_time()
{
    return std::chrono::duration_cast<std::chrono::nanoseconds>(std::chrono::steady_clock::now().time_since_epoch()).count();
}

int main()
{
    ofstream f_l;
    f_l.open("f_l_push.txt");
    forward_list<int> forw_list;
    forw_list.push_front(-1000 + rand() % 2001);
    for(int i = 1; i <= 100000; i++)
    {
        double start_time = 0, end_time = 0;
        start_time = get_time();
        forw_list.push_front(-1000 + rand() % 2001);
        end_time = get_time();
        f_l << end_time - start_time << endl;
    }
    return 0;
}