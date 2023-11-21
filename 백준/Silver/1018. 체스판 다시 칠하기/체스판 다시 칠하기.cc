#include <iostream>
#include <ios>
#include <algorithm>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    
    int N,M;
    cin >> N >> M;
    if(N<8||M<8||N>50||M>50)
        return 0;
    
    char **board;
	board = new char*[N];
	for (int i = 0; i < N; i++)
		board[i] = new char[M];
    
    for(int i=0; i<N; i++)
    {
        for(int j=0; j<M; j++)
        {
            cin >> board[i][j];
        }
    }
    
    int minsum=64;
    for(int i=0; i<=N-8; i++)
    {
        for(int j=0; j<=M-8; j++)
        {
            char chess[8][8];
            for(int y=0; y<8; y++)
            {
                for(int x=0; x<8; x++)
                {
                    chess[y][x]=board[x+i][y+j];
                }
            }
            
            int bsum=0;
            int wsum=0;
            for(int y=0; y<8; y++)
            {
                for(int x=0; x<8; x++)
                {
                    if((!(x%2)&&!(y%2))||((x%2)&&(y%2)))
                        if(chess[y][x]=='B')
                            bsum++;
                        else
                            wsum++;
                    else
                        if(chess[y][x]=='W')
                            bsum++;
                        else
                            wsum++;
                }
            }
            if(minsum>min(wsum,bsum))
            {
                minsum=min(wsum,bsum);
            }
        }
    }
    
    cout << minsum << '\n';
    
    delete [] board;
}