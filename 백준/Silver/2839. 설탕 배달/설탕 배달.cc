#include <iostream>
using namespace std;

int main()
{
    int N;
    cin >> N;
    if(N<3 || N>5000)
        return 0;

    int five=0;
    int three=0;;
    while(N-3*three>=0)
    {
        if((N-3*three)%5==0)
        {
            five=(N-3*three)/5;
            cout<<five+three;
            return 0;
        }
        three++;
    }
    cout << -1;
    return 0;
}