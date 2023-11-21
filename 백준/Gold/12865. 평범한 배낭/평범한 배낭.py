import sys

N, K = map(int, sys.stdin.readline().strip().split())

WV = [[0,0]]
for _ in range(N): 
    WV.append(list(map(int,sys.stdin.readline().strip().split())))

dp = [[0 for _ in range (K+1)] for _ in range (N+1)]

for i in range(N+1):
    for j in range(K+1):
        if WV[i][0]>j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-WV[i][0]]+WV[i][1])

print(max(map(max,dp)))