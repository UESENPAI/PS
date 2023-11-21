#include <iostream>
#include <algorithm>
using namespace std;

int main(void)
{
    const int N=9;
    int arr[N];
    int tmp[N];
    for(int i=1; i<N+1; i++)
    {
        cin >> arr[i-1];
    }
    copy(arr, arr+N, tmp);
    sort(tmp,tmp+N);
    cout << tmp[N-1] << endl;
    for(int i=1; i<N+1; i++)
    {
        if(arr[i-1]==tmp[N-1])
        {
            cout << i;
            break;
        }
    }
}