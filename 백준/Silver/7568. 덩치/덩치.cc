#include <iostream>
#include <ios>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    int N;
    cin >> N;
    if(N<2||N>50)
        return 0;
    vector<pair<int, int>> thug(N);
    int* rank = new int[N];
    
    for(int i=0; i<N; i++)
    {
        cin >> thug[i].first >> thug[i].second;
        if(thug[i].first<10||thug[i].second>200||thug[i].first<0||thug[i].second<0)
            return 0;
    }
    
    for(int i=0; i<N; i++)
    {
        int cnt=0;
        for(int j=0; j<N; j++)
        {
            if(thug[i].first<thug[j].first&&thug[i].second<thug[j].second)
                cnt++;
        }
        rank[i]=cnt+1;
    }
    
    for(int i; i<N; i++)
    {
        cout << rank[i] << ' ';
    }
}