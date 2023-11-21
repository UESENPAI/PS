#include <iostream>
#include <ios>
#include <cmath>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    int T;
    cin >> T;
    while(T--)
    {
        int x1, y1, x2, y2, r1, r2;
        cin >> x1 >> y1 >> r1 >> x2 >> y2 >> r2;
        if(x1<-10000||y1<-10000||x2<-10000||y2<-10000||x1>10000||y1>10000||x2>10000||y2>10000||r1>10000||r2>10000||r1<0||r2<0)
            return 0;
        double dist = sqrt(pow(x1-x2,2)+pow(y1-y2,2));
        if(abs(r2-r1)<dist&&dist<(r2+r1))
           cout << 2 << '\n';
        else if((dist==abs(r2-r1)||dist==(r2+r1))&&dist)
           cout << 1 << '\n';
        else if(dist<abs(r2-r1)||dist>(r1+r2))
           cout << 0 << '\n';
        else if(!dist&&r1==r2)
           cout << -1 << '\n';
    }
}