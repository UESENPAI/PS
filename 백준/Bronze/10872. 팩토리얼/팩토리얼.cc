#include <iostream>
#include <ios>
using namespace std;

int facto(int N)
{
    if(N==1||N==0)
        return 1;
    return N*facto(N-1);
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    int N;
    cin >> N;
    if(N<0||N>12)
        return 0;
    cout << facto(N) << '\n';
}