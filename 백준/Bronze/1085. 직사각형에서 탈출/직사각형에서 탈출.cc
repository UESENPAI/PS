#include <iostream>
#include <ios>
#include <algorithm>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    int x, y, w, h;
    cin >> x >> y >> w >> h;
    if(x<0||y<0||x>1000||y>1000||x<1||x>(w-1)||y<1||y>(h-1))
        return 0;
    int cas[4];
    cas[0]=x;
    cas[1]=y;
    cas[2]=w-x;
    cas[3]=h-y;
    sort(cas, cas+4);
    cout << cas[0] <<'\n';
}
