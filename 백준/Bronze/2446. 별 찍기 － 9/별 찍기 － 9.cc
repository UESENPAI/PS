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
        if(i<N)
        {
            for(int j=0; j<i-1; j++)
            {
                cout << " ";
            }
            for(int j=(2*N-1)-2*(i-1); j>0; j--)
            {
                cout << "*";
            }
        }
        else
        {
            for(int j=2*N-1-i; j>0; j--)
            {
                cout << " ";
            }
            for(int j=1+2*(i-N); j>0; j--)
            {
                cout << "*";
            }
        }
        cout << endl;
    }
}