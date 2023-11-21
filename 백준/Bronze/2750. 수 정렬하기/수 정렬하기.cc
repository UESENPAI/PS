#include <iostream>
#include <ios>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

int main()
{
    int N;
    cin >> N;
    if(N<1||N>1000)
        return 0;
    vector<int> v;
    while(N--)
    {
        int in;
        cin >> in;
        if(abs(in)<1000);
        v.push_back(in);
    }
    sort(v.begin(), v.end());
    for(auto& i : v)
    {
        cout << i << " ";
    }
    return 0;
}