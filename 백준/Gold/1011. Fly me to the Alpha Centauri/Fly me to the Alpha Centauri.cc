#include <iostream>
#include <ios>
#include <cmath>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    int T;
    cin >> T;
    while(T--)
    {
        int x,y,dist,n;
        cin >> x;
        cin >> y;
        if(x<0||x>=y||y>=pow(2,31))
            return 0;
        
        dist=y-x;
        n=1;
        while(dist>=pow(n,2))
        {
            n++;
        }
        n--;
        if(dist==pow(n,2))
            cout << 2*n-1<<'\n';
        else if(dist<=((pow(n,2)+pow(n+1,2))/2))
            cout << 2*n<<'\n';
        else
            cout << 2*n+1<<'\n';
    }
    return 0;
}