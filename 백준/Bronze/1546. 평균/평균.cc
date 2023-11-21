#include <iostream>
#include <algorithm>
using namespace std;

int main(void)
{
    int N;
    cin >> N;
    int score[N];
    float avg=0;
    
    int M=0;
    
    for(int i=1; i<N+1; i++)
    {
        cin >> score[i-1];
        if(score[i-1]>100 || score[i-1]<0)
            return 0;
        avg+=score[i-1]*100;
        if(score[i-1]>M)
            M=score[i-1];
    }
    
    if(M==0) return 0;
    avg/=M;

    cout.precision(4);
    cout << avg/N;
}