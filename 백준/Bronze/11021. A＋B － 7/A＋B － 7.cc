#include <iostream>
using namespace std;

int main(void)
{
    int A,B,T;
    cin >> T;
    for(int i=1; i<=T; i++)
    {
        cin >> A >> B;
        cout << "Case #" << i << ": "<< A+B <<"\n";
    }
}