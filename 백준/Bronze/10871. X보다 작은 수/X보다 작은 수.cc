#include <iostream>
using namespace std;

int main(void)
{
    int N, X;
    cin >> N >> X;
    int tmp[N];
    
    if(1>N||X>10000)
    {
        return 0;
    }
    
    for(int i=1; i<N+1; i++)
    {
        cin >> tmp[i-1];
    }
        
    for(int i=1; i<N+1; i++)
    {
        if(tmp[i-1]<X)
        {
            cout << tmp[i-1] << " ";
        }
    }       
}