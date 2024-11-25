import sys
input = sys.stdin.readline

def boj12865():
    N, K = map(int, input().split())
    bag = [list(map(int, input().strip().split())) for _ in range(N)]
    dp = [[0]*(K+1) for _ in range(N+1)]

    for i in range(1, N+1):
        for j in range(1, K+1):
            dp[i][j] = dp[i-1][j] if j < bag[i-1][0] else max(bag[i-1][1]+dp[i-1][j-bag[i-1][0]],dp[i-1][j])

    print(dp[N][K])

if __name__ == "__main__":boj12865()