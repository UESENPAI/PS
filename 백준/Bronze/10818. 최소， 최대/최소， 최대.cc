#include <iostream>
#include <algorithm>
using namespace std;

int main(void)
{
    int N;
    cin >> N;
    if(N<1 || N>1000000)
        return 0;
    int *arr = new int[N];
    
    for(int i=1; i<N+1; i++)
    {
        cin >> arr[i-1];
        if(arr[i-1]<-1000000||arr[i-1]>1000000);
    }
    sort(arr, arr+N);
    cout << arr[0] << " "<<arr[N-1];
}