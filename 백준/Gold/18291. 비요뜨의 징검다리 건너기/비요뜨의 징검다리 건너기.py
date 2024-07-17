from sys import stdin
input = stdin.readline

def boj18291():
    T = int(input().strip())
    N = [int(input().strip()) for _ in range(T)]
    MOD = 10**9 + 7

    def modpow(base, exp):
        nonlocal MOD
        result = 1
        while exp > 0:
            if exp & 1: result = (result * base) % MOD
            base = (base * base) % MOD
            exp >>= 1
        return result

    for n in N: print(n) if n<2 else print(modpow(2, n-2))       

if __name__ == '__main__': boj18291()