#include <iostream>
using namespace std;

int main(void)
{
    int N;
    cin >> N;
    if(N<1||N>100)
    {
        return 0;
    }
    for(int i=1; i<2*N; i++)
    {
        if(i<=N)
        {
            for(int j=1; j<=i; j++)
            {
                cout<<"*";
            }
        }
        else
        {
            for(int j=2*N-i; j>=1; j--)
            {
                cout<<"*";
            }
        }
        cout << "\n";
    }
}