#include <iostream>
#include <ios>
#include <cmath>
using namespace std;

int is_prime(int N)
{
    if(N==1)
        return false;
    int cnt=0;
    int fin=sqrt(N);
    for(int i=1; i<=fin; i++)
    {
        if(N%i==0)
            cnt++;
    }
    if(cnt>1)
        return false;
    else
        return true;
}

int main()
{
    ios::sync_with_stdio(false);
    int N;
    cin >> N;
    if(N>100)
        return 0;
    int cnt=0;
    while(N--)
    {
        int num;
        cin >> num;
        if(num>1000||num<0)
        {
            return 0;
        }
        
        if(is_prime(num))
            cnt++;
    }
    cout << cnt << '\n';
}