#include <iostream>
#include <algorithm>
using namespace std;

int main(void)
{
    int burger[3];
    int drink[2];      
    for(int i=1; i<4; i++)
    {
        cin >> burger[i-1];
        if(burger[i-1]<100||burger[i-1]>2000)
        {
            return 0;
        }
    }
    sort(burger, burger+3);
    
    for(int i=1; i<3; i++)
    {
        cin >> drink[i-1];
        if(drink[i-1]<100||drink[i-1]>2000)
        {
            return 0;
        }
    }
    sort(drink, drink+2);
    
    cout << drink[0]+burger[0]-50;
    return 0;
}