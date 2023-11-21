import sys

N = int(sys.stdin.readline().strip())
L = list(map(int,sys.stdin.readline().strip().split()))
G = list(map(int,sys.stdin.readline().strip().split()))

ans = 0
tmp = G[0]
for i in range (N-1):
    if tmp > G[i]:
        tmp = G[i]
    ans += tmp * L[i]

print(ans)
