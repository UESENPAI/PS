#include <iostream>
using namespace std;

int main()
{
    int N;
    cin >> N;
    if(N<1||N>1000000000)
        return 0;
    
    int n=1;
    while(1+3*n*(n-1)<N)
    {
        n++;
    }
    cout << n;
}