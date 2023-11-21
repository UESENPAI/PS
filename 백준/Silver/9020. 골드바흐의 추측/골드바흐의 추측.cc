#include <iostream>
#include <ios>
#include <cmath>
using namespace std;

bool is_prime(int N)
{
    if(N==2)
        return true;
    if(N%2==0||N==1)
        return false;
    for(int i=3; i<=sqrt(N); i=i+2)
    {
        if(N%i==0)
            return false;
    }
    return true;
}

int main()
{
    int T,n;
    cin >> T;
    while(T--)
    {
        cin>>n;
        if(n<4||n>10000||n%2!=0)
            break;
        
        for(int i=n/2; i>0; i--)
        {
            if(is_prime(i)&&is_prime(n-i))
            {
               cout << i << ' ' << n-i << '\n';
               break;
            }
        }
    }
}