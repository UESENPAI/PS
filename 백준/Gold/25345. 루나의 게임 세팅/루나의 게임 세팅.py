import sys
from math import factorial
input = sys.stdin.readline

def boj25345():
    N, K = map(int, input().split())
    H = [*map(int, input().strip().split())]
    MOD = 10**9 + 7

    result = (factorial(N) // factorial(N - K) // factorial(K) * (1<<(K - 1))) % MOD
    print(result)

if __name__ == "__main__": boj25345()