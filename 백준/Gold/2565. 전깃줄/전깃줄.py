import sys

N = int(sys.stdin.readline().strip())

w = []
w_b = []
dp = [0 for i in range(N)]
for i in range(N): w.append(list(map(int, input().split())))
w.sort(key = lambda x:x[0])

for i in range(N): w_b.append(w[i][1])
for i in range(N):
    for j in range(i):
        if w_b[i] > w_b[j] and dp[i] < dp[j]: dp[i] = dp[j]
    dp[i] += 1
    
print(N - max(dp))