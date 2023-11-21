import sys

N, K = map(int, sys.stdin.readline().strip().split())
MOD = 1000000007

def mod_pow(x, n, mod):
    if not n: return 1
    elif n%2:
        y = mod_pow(x, n-1, mod)
        return (x * y) % mod
    else:
        y = mod_pow(x, n//2, mod)
        return (y * y) % mod

def mod_factorial(n, mod):
    res = 1
    for i in range(1, n+1):
        res *= i
        res %= mod
    return res

def nCk(n, k, mod):
    if k > n: return 0
    return (mod_factorial(n, mod) * mod_pow((mod_factorial(k, mod) * mod_factorial(n-k, mod)) % mod, mod-2, mod)) % mod

       
print(nCk(N,K,MOD))