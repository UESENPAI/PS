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
    int M, N;
    cin >> M;
    cin >> N;
    if(N>10000||N<0||M>10000||M<0)
        return 0;
    
    int sum=0;
    int min=0;
    for(int i=M; i<N+1; i++)
    {
        if(is_prime(i))
            sum+=i;
        if(!min&&is_prime(i))
            min=i;
    }
    if(sum)
    {
        cout << sum << '\n';
        cout << min << '\n';
    }
    else
        cout << -1 << '\n';
    
}