#include <iostream>
using namespace std;

int d_n(int number)
{
    int tmp=number;
    int num=number;
    while(num>0)
    {
        tmp+=num%10;
        num-=num%10;
        num/=10;
    }
    return tmp;
}

int main(void)
{
    bool is_selfnum[10000];
    fill_n(is_selfnum, 10000, true);
    
    for(int i=1; i<10000+1; ++i)
    {
        int tmp=d_n(i);
        if(tmp<=10000)
        {
            is_selfnum[tmp-1]=false;
        }
    }
    
    for(int i=1; i<10000+1; ++i)
    {
        if(is_selfnum[i-1])
            cout << i << '\n';
    }
    return 0;
}