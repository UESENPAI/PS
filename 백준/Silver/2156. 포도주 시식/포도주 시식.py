import sys

n = int(sys.stdin.readline().strip())

w=[]
w.append(0)
for _ in range(n): w.append(int(sys.stdin.readline().strip()))

dp=[]
dp.append(0)
dp.append(w[1])
if n>1:
    dp.append(w[1]+w[2])
for i in range(3, n+1):
    dp.append(max(dp[i-1], dp[i-3]+w[i-1]+w[i], dp[i-2]+w[i]))

print(dp[n])
