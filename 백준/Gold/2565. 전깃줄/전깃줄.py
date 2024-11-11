import sys
input = sys.stdin.readline

def boj2565():
    N = int(input().strip())
    elins = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: x[0])
    
    dp = [0] * N
    for i in range(N):
        for j in range(i):
            if elins[i][1] > elins[j][1] and dp[i] < dp[j]: dp[i] = dp[j]
        dp[i] += 1
    
    print(N - max(dp))

if __name__ == "__main__":boj2565()