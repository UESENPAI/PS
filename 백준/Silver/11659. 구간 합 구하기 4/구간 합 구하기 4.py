import sys

N, M = map(int, sys.stdin.readline().strip().split())

arr = list(map(int, sys.stdin.readline().strip().split()))

memo=[0]
tmp=0
for a in arr:
    tmp+=a
    memo.append(tmp)

for _ in range(M):
    i, j = map(int, sys.stdin.readline().strip().split())
    print(memo[j]-memo[i-1])