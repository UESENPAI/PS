#include <iostream>
using namespace std;

int main(void)
{
    int n=0;
    int tmp=0;
    cin >> n;
    
    for(int i=0; i<=n; i++)
    {
        tmp+=i;
    }
    cout << tmp;
}