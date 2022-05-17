#include<iostream>
#include<set>
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
    ofstream s;
    s.open("set.txt");
    set<int>seT;
    for(int i = 1; i <= 100000; i++)
    {
        double start_time = 0, end_time = 0;
        seT.insert(i);
        set<int>::iterator it_set = seT.begin();
        start_time = get_time();
        while(it_set != seT.end())
        {
            it_set++;
        }
        end_time = get_time();
        s << end_time - start_time << endl;
        cout<<i<<endl;
    }
}
