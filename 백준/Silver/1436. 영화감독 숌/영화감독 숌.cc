#include <iostream>
#include <string>
using namespace std;

int main()
{
    int N;
    cin >> N;
    if(N<0||N>10000)
        return 0;
    int const M=N;
    int beastnum=665;
    int count = 0;
    while(beastnum++)
    {
        string str = to_string(beastnum);
        
        if(str.find("666")!=string::npos)
        {
            count++;
        }
        
        if(M==count)
        {
            cout<<beastnum<<'\n';
            break;
        }
    }
    return 0;
}
