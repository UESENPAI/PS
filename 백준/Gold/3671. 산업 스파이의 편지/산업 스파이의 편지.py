from sys import stdin
from math import sqrt
from itertools import permutations
input = stdin.readline

def boj3671():
    c = int(input().strip())
    tcs = [tuple(input().strip()) for _ in range(c)]

    def is_prime(n):
        if n < 2: return False
        if n == 2: return True
        if not n&1: return False
        for i in range(3, int(sqrt(n)+1), 2):
            if not n % i: return False
        return True

    for tc in tcs:
        primes = set()
        for dlen in range(1, len(tc)+1):
            for p in permutations(tc, dlen):
                n = int(''.join(p))
                if is_prime(n): primes.add(n)
        print(len(primes))

if __name__ == '__main__': boj3671()