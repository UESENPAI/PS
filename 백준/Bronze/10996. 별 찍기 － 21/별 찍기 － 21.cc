#include <iostream>
using namespace std;

int main(void)
{
    int N;
    cin >> N;
    
    if(N<0 || N>100)
    {
        return 0;
    }
    
    for(int i=1; i<2*N+1; i++)
    {
        if(i%2==1)
        {
            cout << "*";
            if(N%2==0)
            {
                for(int j=N/2-1; j>0; j--)
                {
                    cout << " *";
                }
            }
            else
            {
                for(int j=(N+1)/2-1; j>0; j--)
                {
                    cout << " *";
                }
            }
        }
        else
        {
           if(N%2==0)
            {
                for(int j=N/2; j>0; j--)
                {
                    cout << " *";
                }
            }
            else
            {
                for(int j=(N+1)/2-1; j>0; j--)
                {
                    cout << " *";
                }
            } 
        }
        cout << endl;
    }
}