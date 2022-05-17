#include<iostream>
#include<vector>
#include<ctime>
#include<cstdlib>
#include<fstream>
using namespace std;
int main()
{
    vector<int>arr;
    ofstream cap,siz;
    cap.open("cap.txt");
    siz.open("siz.txt");
    for(int i = 1; i < 100000; i++)
    {
        arr.push_back(-1000 + rand() % 2001);
        cap << arr.capacity() << endl;
        siz << arr.size() <<endl;
    }
}
