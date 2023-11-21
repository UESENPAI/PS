#include <iostream>
#include <ios>
#include <vector>
using namespace std;

int main()
{
    int N;
    cin >> N;
    if(N<1||N>1000000)
        return 0;
    bool endgame=true;
    for(int i=1; i<=N; i++)
    {
        int sum=i;
        int onum = i;
        while(onum>10)
        {
            sum+=onum%10;
            onum-=onum%10;
            onum/=10;
        }
        sum+=onum;
        if(sum==N)
        {
            cout << i << '\n';
            endgame=false;
            break;
        }
    }
    if(endgame) cout << 0 << '\n';
}