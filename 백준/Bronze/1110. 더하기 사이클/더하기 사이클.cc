#include <iostream>
using namespace std;

int main(void)
{
    int N, tmp, new_num, cycle_length;
    cycle_length=0;
    cin >> N;
    
    if(N<10)
    {
        N*=10;
    }
    
    new_num=N;
    
    if(N<0||N>99)
        return 0;
    
    while(true)
    {
        tmp=(new_num-(new_num%10))/10 + (new_num%10);
        new_num=(new_num%10)*10+(tmp%10);
        cycle_length++;

        if(new_num==N)
        {
            cout << cycle_length;
            break;
        }
    } 
}