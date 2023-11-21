#include <iostream>
#include <string>
using namespace std;

int main(void)
{
    int tcse_num, cnt, tmp_sum;
    cin >> tcse_num;
    string score;
    
    for(int i=1; i<tcse_num+1; i++)
    {
        cnt=0;
        tmp_sum=0;
        cin >> score;
        if(score.length()<0||score.length()>80+1)
            return 0;
        for(int inx=0; inx<score.length(); inx++)
        {
            if(score[inx]=='O')
                cnt+=(++tmp_sum);
            else
                tmp_sum=0;            
        }
        cout << cnt << '\n';
    }
    return 0;
}
