import sys

T = int(sys.stdin.readline().strip())

dp = [0 for _ in range(101)]
dp[0] = dp[1] = dp[2] = 1
for _ in range(T):
    N = int(sys.stdin.readline().strip())
    for n in range(3, N+1):
        if not dp[n]:
            dp[n] = dp[n-2]+dp[n-3]
    print(f'{dp[N-1]}')
