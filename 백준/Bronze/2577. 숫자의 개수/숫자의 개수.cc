#include <iostream>
#include <vector>
using namespace std;

int main(void)
{
    int A,B,C;
    cin >> A;
    cin >> B;
    cin >> C;
    if(A<100 || B<100 || C<100 || A>=1000 || B>= 1000 || C>= 1000)
        return 0;
    int tmp=A*B*C;
    int num_cnt[10];
    fill_n(num_cnt, 10, 0);
    
    while(tmp>0)
    {
        num_cnt[tmp%10]++;
        tmp-=(tmp%10);
        tmp/=10;
    }
    
    for(int i=0; i<10; i++)
    {
        cout << num_cnt[i] << "\n";
    }
}