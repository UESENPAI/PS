#include <iostream>
#include <ios>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int T,N,H,W;
    cin >> T;
    while(T--)
    {
        cin >> H >> W >> N;
        if(H<1||W<1||H>99||W>99||N<1||N>H*W)
            return 0;
        
        int num_floor=N%H;
        if(!num_floor)
            num_floor=H;
        int num_room=(N-num_floor)/H+1;

        
        cout << num_floor*100+num_room << "\n";
    }
}