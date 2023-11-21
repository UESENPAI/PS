#include <iostream>
using namespace std;

int main()
{
    int N, M;
    int A[100];
    cin >> N >> M;
    int result=0;
    for (int i = 0; i < N; i++) cin >> A[i];
    
    for (int i = 0; i < N-2; i++)
    {
        for (int j = i + 1; j < N-1; j++)
        {
            for (int k = j + 1; k < N; k++)
            {
                if (A[i] + A[j] + A[k] <= M && M-(A[i] + A[j] + A[k]) < M-result)
                {
                    result = A[i] + A[j] + A[k];
                }
            }
        }
    }
    cout << result;
}