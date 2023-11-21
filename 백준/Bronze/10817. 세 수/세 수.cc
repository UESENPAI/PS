#include <iostream>
#include <algorithm>
using namespace std;

int main(void)
{
    int A,B,C;
    cin >> A >> B >> C;
    int tmp[3];
    tmp[0]=A;
    tmp[1]=B;
    tmp[2]=C;
    if(A<1 || B<1 || C<1 || A>100 || B>100 || C>100)
    {
        return 0;
    }
   sort(tmp, tmp+3);
   cout << tmp[1];
}