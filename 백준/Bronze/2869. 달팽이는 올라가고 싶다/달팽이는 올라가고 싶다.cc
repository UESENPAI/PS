#include <iostream>
#include <ios>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    int A, B, V;
    cin >> A >> B >> V;
    if(B<1||A<B||V<A||V>1000000000)
        return 0;
    int day=(V-A)/(A-B);
    while((V-A)-(A-B)*day>0)
    {
        day++;
    }
    cout << ++day;
}