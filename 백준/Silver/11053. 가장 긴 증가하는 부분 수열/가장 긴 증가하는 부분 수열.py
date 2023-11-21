import sys

N = int(sys.stdin.readline().strip())

A=[]
A=list(map(int,sys.stdin.readline().strip().split()))
A.insert(0,0)

dp=[0 for _ in range(N+1)]
for i in range(1,N+1):
    for j in range(i):
        if A[i] > A[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i]+=1

print(max(dp))
