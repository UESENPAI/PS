#include <iostream>
#include <ios>
#define _USE_MATH_DEFINES
#include <cmath>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    int R;
    cin >> R;
    if(R<0||R>10000)
        return 0;
    cout<<fixed;
    cout.precision(6);
    cout << pow(R,2)*M_PI << '\n';
    cout << pow(R,2)*2 << '\n';
}