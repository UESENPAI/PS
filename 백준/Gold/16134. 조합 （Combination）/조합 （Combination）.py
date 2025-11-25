from sys import stdin
input = stdin.readline

def boj16134():
    N, R = map(int, input().split())
    MOD = 1000000007

    def modpow(a, b):
      result = 1
      while b:
          if b & 1:
              result = result * a % MOD
          a = a * a % MOD
          b >>= 1
      return result

    fact = [1] * (N + 1)
    for i in range(1, N + 1):
        fact[i] = fact[i-1] * i % MOD

    num = fact[N]
    den = fact[R] * fact[N-R] % MOD
    ans = num * modpow(den, MOD - 2) % MOD

    print(ans)

if __name__ == '__main__': boj16134()