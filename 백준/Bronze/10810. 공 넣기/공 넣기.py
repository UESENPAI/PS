import sys

N, M = map(int,sys.stdin.readline().strip().split())

bsk = [0 for _ in range(N)]

for _ in range(M):
    i, j, k = map(int,sys.stdin.readline().strip().split())
    for idx in range(i, j+1):
        bsk[idx-1] = k

print(*bsk)