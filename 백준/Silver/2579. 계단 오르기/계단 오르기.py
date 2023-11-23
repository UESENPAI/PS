import sys
input = sys.stdin.readline

def boj2579(N, stairs):
    if N == 1: return stairs[0]
    elif N == 2: return stairs[0] + stairs[1]
    
    dp = [0 for _ in range(N)]
    dp[0], dp[1] = stairs[0], stairs[0] + stairs[1]
    
    for i in range(2, N): dp[i] = max(dp[i-2] + stairs[i], dp[i-3] + stairs[i-1] + stairs[i])
    
    return dp[-1]

if __name__ == "__main__":
    N = int(input().strip())
    stairs = [int(input().strip()) for _ in range(N)]
    print(boj2579(N, stairs))
