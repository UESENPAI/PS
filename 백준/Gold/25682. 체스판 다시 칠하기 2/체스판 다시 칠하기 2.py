import sys

N, M, K = map(int,sys.stdin.readline().strip().split())

chs = []
for _ in range(N): chs.append(sys.stdin.readline().strip())     
dp_black = [[0 for _ in range(M+1)] for _ in range(N+1)]
dp_white = [[0 for _ in range(M+1)] for _ in range(N+1)]

for row in range(1, N+1):
    for col in range(1, M+1):
        if (row == col) or not (row+col)%2:
            if chs[row-1][col-1] == 'B': dp_white[row][col] = 1
            else: dp_black[row][col] = 1
        else:
            if chs[row-1][col-1] == 'B': dp_black[row][col] = 1
            else: dp_white[row][col] = 1

        dp_black[row][col] += dp_black[row-1][col] + dp_black[row][col-1] - dp_black[row-1][col-1]
        dp_white[row][col] += dp_white[row-1][col] + dp_white[row][col-1] - dp_white[row-1][col-1]

cnt = K**2+1
for i in range(1, N-K+2):
    for j in range(1, M-K+2):
        bcnt = dp_black[i+K-1][j+K-1]-dp_black[i+K-1][j-1]-dp_black[i-1][j+K-1]+dp_black[i-1][j-1]
        wcnt = dp_white[i+K-1][j+K-1]-dp_white[i+K-1][j-1]-dp_white[i-1][j+K-1]+dp_white[i-1][j-1]
        cnt = min(cnt,bcnt,wcnt)
print(cnt)
