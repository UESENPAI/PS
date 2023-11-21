#include <iostream>
#include <ios>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    int N;
    cin >> N;
    if(N>1000000000||N<0)
        return 0;
    vector<int> v;
    while(N>0)
    {
        v.push_back(N%10);
        N-=N%10;
        N/=10;
    }
    sort(v.begin(),v.end());
    
    for(int i=v.size()-1; i>=0; i--)
    {
        cout << v[i];
    }
}