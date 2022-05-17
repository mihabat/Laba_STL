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
    v.open("vector.txt");
    vector<int>vec;
    for(int i = 1; i <= 100000; i++)
    {
        double start_time = 0, end_time = 0;
        vec.push_back(-1000 + rand() % 2001);
        start_time = get_time();
        for(int j = 0; j < vec.size(); j++)
        {
            vec[j]++;
        }
        end_time = get_time();
        v << end_time - start_time << endl;
        cout<<i<<endl;
    }
}
