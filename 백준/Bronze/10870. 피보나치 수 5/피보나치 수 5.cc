#include <iostream>
#include <ios>
#include <vector>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    int n;
    cin >> n;
    if(n<0||n>20)
        return 0;
    vector<int> fibo;
    fibo.push_back(0);
    fibo.push_back(1);
    for(int i=2; i<22; i++)
    {
        fibo.push_back(fibo[i-2]+fibo[i-1]);
    }
    cout << fibo[n] << '\n';
}