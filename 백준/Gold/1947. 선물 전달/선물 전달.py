import sys
input = sys.stdin.readline

def boj1947():
    N = int(input().strip())

    def getDerangement(N):
        if N == 1: return 0
        elif N == 2: return 1
        else:
            MOD = 1000000000
            dp = [0] * (N + 1)
            dp[1], dp[2] = 0, 1

            for i in range(3, N + 1):
                dp[i] = (i - 1) * (dp[i-1] + dp[i-2]) % MOD
            
            return dp[N]

    print(getDerangement(N))
                 
if __name__ == '__main__': boj1947()