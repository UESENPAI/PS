#include <iostream>
using namespace std;

int main(void)
{
    int arr[10];
    bool res[42];
    fill_n(res,42,false);
    for(int i=1; i<10+1; i++)
    {
        cin >> arr[i-1];
        if(arr[i-1]>1000||arr[i-1]<0)
            return 0;
        if(!res[arr[i-1]%42])
            res[arr[i-1]%42]=true;
    }
    int tmp=0;
    for(int i=0; i<42; i++)
        if(res[i])
            tmp++;
    cout << tmp;
}