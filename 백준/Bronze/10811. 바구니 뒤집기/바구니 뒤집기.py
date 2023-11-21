import sys

N, M = map(int,sys.stdin.readline().strip().split())

bsk = [i for i in range(0,N+1)]

def rev_bsk(i,j):
    global bsk
    if (j-i)%2:
        for p in range((j-i)//2 + 1):
            bsk[i+p], bsk[j-p] = bsk[j-p], bsk[i+p]
    else:
        for p in range((j-i)//2):
            bsk[i+p], bsk[j-p] = bsk[j-p], bsk[i+p]

for _ in range(M):
    i, j = map(int,sys.stdin.readline().strip().split())
    rev_bsk(i,j)

for i in range(1, N+1): print(f'{bsk[i]}', end=" ")
