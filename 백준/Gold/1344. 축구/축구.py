import sys
from math import comb, sqrt
input = sys.stdin.readline

def boj2086():
    A = int(input().strip()) / 100
    B = int(input().strip()) / 100
    n = 18
   
    primes = {2, 3, 5, 7, 11, 13, 17}

    getprob = lambda p, n, k: comb(n, k) * pow(p, k) * pow(1 - p, n - k)

    probA = [getprob(A, n, i) for i in range(n+1)]
    probB = [getprob(B, n, i) for i in range(n+1)]

    probZ = 0
    for i in range(n+1):
        for j in range(n+1):
            if i not in primes and j not in primes:
                probZ += probA[i] * probB[j]
    ans = 1 - probZ
    print(ans)

if __name__ == '__main__': boj2086()