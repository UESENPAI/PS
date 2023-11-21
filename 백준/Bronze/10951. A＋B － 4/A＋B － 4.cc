#include <iostream>
using namespace std;

int main(void)
{
    int A,B;
    
    while(cin >> A >> B)
    {
        if(A<=0||A>=10||B<=0||B>=10)
            return 0;
        cout << A+B << endl;
    }
    
    return 0;
}