#include <iostream>
#include <ios>
using namespace std;

int getNum(int a, int b)
{
    if(b==1)
        return 1;
    if(a==0)
        return b;
    return (getNum(a-1,b)+getNum(a,b-1));
}

int main()
{
    ios::sync_with_stdio(false);
    int T,n,k;
    cin >> T;
    while(T--)
    {
        cin >> n;
        if(n<1||n>14)
            return 0;
        cin >> k;
        if(k<1||k>14)
            return 0;
        
        cout << getNum(n,k)<<'\n';
    }
}