import sys
from math import lcm, gcd
input = sys.stdin.readline

def factorization(a):
    factors = {}
    prime = 2
    while not prime * prime > a:
        if not a % prime:
            factors[prime] = 0
            while not a % prime:
                factors[prime] += 1
                a //= prime
        prime += 1
    if a > 1: factors[a] = 1
    return factors

def boj16888():
    a, b, L = map(int, input().strip().split())
    lcm_ab = lcm(a, b)
    
    if L % lcm_ab:
        print(-1)
        return
    
    L_factor = factorization(L)
    lcm_ab_factor = factorization(lcm_ab)
    
    c = 1
    for prime, count in L_factor.items():
        if prime in lcm_ab_factor:
            if lcm_ab_factor[prime] < count:c *= prime ** count
            elif lcm_ab_factor[prime] > count:
                print(-1)
                return
        else:
            c *= prime ** count

    print(c)

if __name__ == "__main__": boj16888()