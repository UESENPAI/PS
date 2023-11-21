#include <iostream>
#include <vector>
using namespace std;

bool is_hansu(int num)
{
    if(num<100)
        return true;
    
    int number=num;
    
    vector<int> numvec;
    while(number>0)
    {
        numvec.push_back(number%10);
        number-=(number%10);
        number/=10;
    }
    
    bool tmp=false;
    for(int i=2; i<numvec.size(); i++)
    {
        if(numvec[i-1]-numvec[i]==numvec[i-2]-numvec[i-1])
            tmp=true;
        else
            tmp=false;
    }
    numvec.clear();
    return tmp;
}

int main(void)
{
    int N;
    cin >> N;
    if(N>1000||N<1)
        return 0;
    int cnt=0;
    for(int i=1; i<N+1; i++)
    {
        if(is_hansu(i))
            cnt++;
    }
    cout << cnt;
    return 0;
}