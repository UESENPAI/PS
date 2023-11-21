#include <iostream>
using namespace std;

int main(void)
{
    int N;
    cin >> N;
    for(int i=1; i<=N; i++)
    {
       for(int s=1; s<(N-i+1); s++)
       {
           cout << " ";
       }
       for(int j=1; j<=i; j++)
       {
           cout << "*";
       }
       cout << "\n";
    }
}