import sys
from math import inf
input = sys.stdin.readline

N = int(input())
s = [list(map(int, input().split())) for _ in range(N)]
DP = [[0 for _ in range (N)] for _ in range(N)]

for col in range(1, N):
    for row in range(N - col):
        mid = row + col
        DP[row][mid] = inf
        for k in range(row, mid):
            DP[row][mid] = min(DP[row][mid], DP[row][k] + DP[k + 1][mid] + s[row][0] * s[k][1] * s[mid][1])
            #print(f'col={col}, row={row}, mid={mid}')
            #print(f'DP[row][mid] = min(DP[{row}][{mid}], DP[{row}][{k}] + DP[{k + 1}][{mid}] + s[{row}][0] * s[{k}][1] * s[{mid}][1])')
            #print(f'{DP[row][mid]} = min({DP[row][mid]}, {DP[row][k]} + {DP[k + 1][mid]} + {s[row][0]} * {s[k][1]} * {s[mid][1]})')
print(DP[0][N - 1])
