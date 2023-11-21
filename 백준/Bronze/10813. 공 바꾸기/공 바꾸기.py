import sys

N, M = map(int,sys.stdin.readline().strip().split())

bsk = [i for i in range(1,N+1)]

for _ in range(M):
    i, j = map(int,sys.stdin.readline().strip().split())
    bsk[i-1], bsk[j-1] = bsk[j-1], bsk[i-1]

print(*bsk)