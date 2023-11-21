#include <iostream>
#include <ios>
#include <cmath>
using namespace std;

void star(int i, int j, int num)
{
    if((i / num)%3 == 1 && (j / num)%3 == 1) {
        cout << ' ';
    }
    else
    {
        if(num / 3 == 0)
            cout <<'*';
        else
            star(i,j,num/3);
    }
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    
    int N;
    cin >> N;
    if(N%3!=0||N<3||N>pow(3,8))
        return 0;
    
    for(int i = 0; i < N; i++)
    {
        for(int j = 0; j < N; j++)
            star(i,j,N);
        cout << '\n';
    }
}