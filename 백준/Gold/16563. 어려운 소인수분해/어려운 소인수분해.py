import sys
input = sys.stdin.readline

def boj16563():
    N = int(input().strip())
    k = list(map(int, input().strip().split()))

    def getprimes(num):
        isprime = [True] * (num + 1)
        isprime[0] = isprime[1] = False
        p = 2
        while (p * p <= num):
            if (isprime[p] == True):
                for i in range(p * p, num+1, p): isprime[i] = False
            p += 1
        primes = [p for p in range(num + 1) if isprime[p]]
        return primes

    primes = getprimes(max(k))

    for ki in k:
        factors = []
        for prime in primes:
            if prime * prime > ki: break
            while not (ki % prime):
                factors.append(prime)
                ki //= prime
        if ki > 1: factors.append(ki)
        print(*factors)

if __name__ == '__main__': boj16563()