#include <iostream>
#include <ios>
#include <vector>
#include <algorithm>
using namespace std;

int main(void){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int N;
    cin>>N;
    if(N<1||N>100000)
        return 0;
    vector<vector<int>> arr(N, vector<int>(2,0));
    for(int i=0; i<N; i++)
    {
        cin>>arr[i][1];
        cin>>arr[i][0];
        if(arr[i][1]<-100000||arr[i][1]>100000||arr[i][0]<-100000||arr[i][0]>100000)
            return 0;
    }
    sort(arr.begin(),arr.end());

    for(int i = 0; i < arr.size(); i++){
        cout<<arr[i][1]<<" "<<arr[i][0]<<'\n';
    }

}