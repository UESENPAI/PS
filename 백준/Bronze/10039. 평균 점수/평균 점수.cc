#include <iostream>
using namespace std;

int main(void)
{
    int score[5];
    int avg=0;
    for(int i=1; i<6; i++)
    {
        cin >> score[i-1];
        
        if(score[i-1]<0||score[i-1]>100||((score[i-1]%5)!=0))
        {
            return 0;
        }
           
        if(score[i-1]<40)
        {
            score[i-1]=40;
        }
        avg+=score[i-1]/5;
    }
    cout << avg;
    return 0;
}