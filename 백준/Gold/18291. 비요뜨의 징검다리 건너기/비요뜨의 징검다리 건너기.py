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

    for n in N:
        if n<2: print(n)
        else:
            exp = (n-2) % (MOD-1)
            print(modpow(2, exp))       

if __name__ == '__main__': boj18291()