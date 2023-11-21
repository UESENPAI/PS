import sys

N, M = map(int, sys.stdin.readline().strip().split())
A = list(map(int, sys.stdin.readline().strip().split()))
res = [0 for _ in range(M)]
res[0] = 1

subsum = 0
for a in range(len(A)):
    subsum +=A[a]
    r=subsum%M
    res[r]+=1

ans = 0
for r in res:
    ans+=r*(r-1)//2
    
print(ans)
