#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    int A, B, C;
    cin >> A >> B >> C;
    if(A<0||B<0||C<0||A>2100000000||B>2100000000||C>2100000000)
        return 0;
    
    if(B>=C)
        cout << -1;
    else
        cout << (A/(C-B))+1;
    return 0;
}