import sys
input = sys.stdin.readline

def boj15824():
    N = int(input().strip())
    scoville = sorted(tuple(map(int, input().strip().split())))
    MOD = 1000000007
    
    agony = 0
    for i in range(N):
        agony += scoville[i] * ((1 << i) - (1 << (N-i-1)))
        agony %= MOD
    
    print(agony % MOD)
    
if __name__ == '__main__': boj15824()