import sys
input = sys.stdin.readline

def boj1328():
    N, L, R = map(int, input().strip().split())
    
    def getdp(N, L, R):
        dp = [[[0] * (N + 1) for _ in range(N + 1)] for _ in range(N + 1)]
        dp[1][1][1] = 1
        
        for n in range(2, N + 1):
            for l in range(1, L + 1):
                for r in range(1, R + 1):
                    dp[n][l][r] = dp[n - 1][l - 1][r] + dp[n - 1][l][r - 1] + dp[n - 1][l][r] * (n - 2)

        print(dp[N][L][R]%1000000007)

    getdp(N, L, R)

if __name__ == '__main__': boj1328()