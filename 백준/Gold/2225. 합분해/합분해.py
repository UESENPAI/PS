import sys
input = sys.stdin.readline

def boj2225():
    N, K = map(int,input().strip().split())

    dp = [[1]*(K+1) for _ in range (N+1)]

    for n in range(1, N+1):
        for k in range(2, K+1):
            dp[n][k] = dp[n-1][k]+dp[n][k-1]
    print(dp[N][K] % 1000000000)

if __name__ == "__main__": boj2225()
