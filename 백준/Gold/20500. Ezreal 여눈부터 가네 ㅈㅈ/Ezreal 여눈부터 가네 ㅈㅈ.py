import sys
input = sys.stdin.readline

def boj20500():
    N = int(input().strip())
    mod = 1000000007

    dp = [0] * (N + 1)
    for i in range(2, N + 1): dp[i] = ((dp[i-1]<<1) - 1) % mod if i&1 else ((dp[i-1]<<1) + 1) % mod
    print(dp[N])

if __name__ == '__main__': boj20500()