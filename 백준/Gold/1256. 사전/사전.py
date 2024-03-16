import sys
from math import factorial
input = sys.stdin.readline

def Combination(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))

def boj1256():
    N, M, K = map(int, input().strip().split())

    def C(n, k): return factorial(n) // (factorial(k) * factorial(n - k))
    
    if K > Combination(N + M, N):
        print(-1)
        return
    
    result = ""
    while N > 0 and M > 0:
        a_count = Combination(N + M - 1, N - 1)
        if K <= a_count:
            result += 'a'
            N -= 1
        else:
            result += 'z'
            M -= 1
            K -= a_count

    result += 'a' * N + 'z' * M
    print(result)

if __name__ == '__main__': boj1256()