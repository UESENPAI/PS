import sys
input = sys.stdin.readline

def boj1720():

    N = int(input().strip())
    
    if N == 1: ans = 1
    elif N == 2: ans = 3
    else:
        dp = [0] * (N + 1)
        dp[1], dp[2] = 1, 3
        for i in range(3, N + 1): dp[i] = dp[i-1] + (dp[i-2]<<1)
        ans = (dp[N] + dp[N>>1])>>1 if N & 1 else (dp[N] + dp[N>>1] + (dp[(N>>1) - 1]<<1)) >> 1

    print(ans)

if __name__ == '__main__': boj1720()