import sys
from math import isqrt

input = sys.stdin.readline

def boj20946():
    N = int(input().strip())
    
    def isprime(N):
        if N == 1: return False
        for i in range(2, isqrt(N)+1):
            if not N % i: return False
        return True

    def getfactors(N):
        factors = []
        temp, i = N, 2

        while temp != 1 and i < isqrt(N)+1:
            if not temp % i:
                factors.append(i)
                temp //= i
            elif i == 2: i += 1
            else: i += 2

        if temp != 1 and isprime(temp): factors.append(temp)
        
        return factors

    if isprime(N): print(-1)
    else:
        factors = getfactors(N)
        combined = []
        for even, odd in zip(factors[::2], factors[1::2]):
            combined.append(even * odd)

        if len(factors) % 2:
            if combined: combined[-1] *= factors[-1]
            else: combined.append(factors[-1])
            
        print(" ".join(map(str, combined)))

if __name__ == "__main__": boj20946()