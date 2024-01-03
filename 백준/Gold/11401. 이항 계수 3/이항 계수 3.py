import sys
from functools import lru_cache
input = sys.stdin.readline

def boj11401():
    N, K = map(int,input().strip().split())
    div = 1000000007

    @lru_cache
    def factorial(N):
        tmp = 1
        for i in range(2, N + 1):
            tmp *= i
            tmp %= div
        return tmp

    def square(N, K):
        if not K: return 1
        elif K == 1: return N
        tmp = square(N, K // 2)
        if K % 2: return tmp**2 * N % div
        else: return tmp**2 % div

    denominator = factorial(N)
    numerator = factorial(N - K) * factorial(K) % div

    print(denominator * square(numerator, div-2) % div)

if __name__ == '__main__': boj11401()