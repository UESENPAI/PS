import sys
input = sys.stdin.readline

def boj15824():
    N = int(input().strip())
    scoville = sorted(tuple(map(int, input().strip().split())))
    MOD = 1000000007

    def pow(a, b):
        if not b: return 1
        elif b == 1: return a
        else:
            half = pow(a, b>>1)
            return half*half*a%MOD if b&1 else half*half%MOD
    
    agony = 0
    for i in range(N):
        #agony += scoville[i] * ((1 << i) - (1 << (N-i-1)))
        agony += scoville[i] * (pow(2, i) - pow(2, N - i - 1))
        agony %= MOD
    
    print(agony % MOD)
    
if __name__ == '__main__': boj15824()  