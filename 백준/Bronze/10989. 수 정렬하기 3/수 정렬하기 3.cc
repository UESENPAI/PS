#include <iostream>
using namespace std;
int main(void) {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int N, temp;
    int countArr[10001] = {0,};
    cin>>N;
    for(int i = 0; i < N; i++){
        cin>>temp;
        countArr[temp]++;
    }

    for(int j = 1; j < 10001; j++)
        countArr[j] += countArr[j-1];
    
    int k = 1;
    while(1){
        if(k > 10000)
            break;
        if(countArr[k] > countArr[k-1]){
            cout<<k<<'\n';
            countArr[k-1]++;
        }
        else
            k++;
    }
}