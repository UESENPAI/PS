from sys import stdin
from math import isqrt
input = stdin.readline

def boj16400():
    N = int(input().strip())
    MOD = 123456789

    is_prime = [True] * (N + 1)
    is_prime[0], is_prime[1] = False, False
    
    for i in range(2, isqrt(N) + 1):
        if is_prime[i]:
            for j in range(i*i, N + 1, i): is_prime[j] = False
    
    primes = [i for i, prime in enumerate(is_prime) if prime]
    
    dp = [0] * (N + 1)
    dp[0] = 1
    for prime in primes:
        for i in range(prime, N + 1):
            dp[i] = (dp[i] + dp[i - prime]) % MOD
    
    print(dp[N])

if __name__ == '__main__': boj16400()