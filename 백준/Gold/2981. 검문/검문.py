import sys
from math import gcd
from math import sqrt

N = int(sys.stdin.readline().strip())

narr = []
for _ in range(N):
    narr.append(int(sys.stdin.readline().strip()))

newarr = []
for i in range(1, N):
    newarr.append(narr[i]-narr[i-1])

tmp = newarr[0]
for i in range(1, len(newarr)):
    tmp = gcd(tmp, newarr[i])

ans = []
for i in range(2, int(sqrt(tmp))+1):
    if tmp % i == 0:
        ans.append(i)
        ans.append(tmp//i)
ans.append(tmp)
ans=list(set(ans))
ans.sort()
print(*ans)