import sys
from math import gcd
input = sys.stdin.readline

def boj1153():
    N = int(input().strip())

    if N < 8:
        print(-1)
        return

    def getprimes(N):
        isprime = [True] * (N+1)
        isprime[0] = isprime[1] = False
        
        p = 2
        while not (p * p > N):
            if (isprime[p]):
                for i in range(p * p, N + 1, p): isprime[i] = False
            p += 1
        
        primes = [p for p, prime in enumerate(isprime) if prime]
        return primes, isprime

    primes, isprime = getprimes(N)

    def get2primes(s):
        for prime in primes:
            if prime > s:
                break
            if isprime[s - prime]:
                return (prime, s - prime)
        return None

    if N % 2:
        tmp = 5
        prefix = (2, 3)
    else:
        tmp = 4
        prefix = (2, 2)

    result = get2primes(N - tmp)

    print(prefix[0], prefix[1], result[0], result[1]) if result else print(-1)

if __name__ == '__main__': boj1153()