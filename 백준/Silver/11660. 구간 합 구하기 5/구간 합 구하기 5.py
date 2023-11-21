import sys

N, M = map(int,sys.stdin.readline().strip().split())

table = []
for _ in range(N):
    table.append(list(map(int,sys.stdin.readline().strip().split())))

dp = [[0 for _ in range(N+1)] for _ in range(N+1)]
for col in range(1,N+1):
    for row in range(1,N+1):
        dp[col][row] = table[col-1][row-1] + dp[col-1][row] + dp[col][row-1] - dp[col-1][row-1]

for _ in range(M):
    x1, y1, x2, y2 = map(int,sys.stdin.readline().strip().split())
    ans = dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1] 
    print(ans)