from sys import stdin
input = stdin.readline

def boj22943():
    K, M = map(int, input().split())

    def sieve(n):
        from math import isqrt
        is_prime = [True] * (n+1)
        if n >= 0: is_prime[0] = False
        if n >= 1: is_prime[1] = False
        for i in range(2, isqrt(n) + 1):
            if is_prime[i]:
                for j in range(i * i, n + 1, i): is_prime[j] = False
        primes = [i for i, v in enumerate(is_prime) if v]
        return is_prime, primes

    from itertools import permutations

    max_n = int(''.join(map(str, range(9, 9 - K, -1))))
    is_prime, primes = sieve(max_n)

    cond1 = [False] * (max_n + 1)
    L = len(primes)
    for i in range(L):
        pi = primes[i]
        for j in range(i + 1, L):
            s = pi + primes[j]
            if s > max_n:
                break
            cond1[s] = True

    ans = 0
    for tup in permutations(range(10), K):
        if tup[0] == 0:
            continue
        x = 0
        for d in tup:
            x *= 10 
            x += d

        if not cond1[x]: continue

        y = x
        while not y % M: y //= M

        ok2 = 0
        for p in primes:
            if p * p > y: break
            if not y % p and is_prime[y // p]:
                ok2 = 1
                break

        ans += ok2

    print(ans)

if __name__ == '__main__': boj22943()