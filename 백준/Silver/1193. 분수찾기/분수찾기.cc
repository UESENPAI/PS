#include <iostream>
using namespace std;

int main()
{
    int X;
    cin >> X;
    if(X<1 || X>10000000)
        return 0;
    
    int n=1;
    while(n*(n-1)/2<X)
    {
        n++;
    }
    n--;
    int m=X-n*(n-1)/2;
    n++;
    if(n%2!=0)
        cout << m <<"/"<< n-m;
    else
        cout << n-m <<"/"<< m;
}