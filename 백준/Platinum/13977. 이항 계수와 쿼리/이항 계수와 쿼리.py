import sys
input = sys.stdin.readline

def boj13977():
    M = int(input().strip())
    NK = [tuple(map(int, input().strip().split())) for _ in range(M)]
    MOD = 1000000007

    get_fermat = lambda a, p: pow(a, p - 2, p)

    def get_fact_n_ifact(max_n):
        nonlocal MOD
        fact, ifact = [1] * (max_n + 1), [1] * (max_n + 1)
        for i in range(2, max_n + 1): fact[i] = fact[i - 1] * i % MOD
        ifact[max_n] = get_fermat(fact[max_n], MOD)
        for i in range(max_n - 1, 0, -1): ifact[i] = ifact[i + 1] * (i + 1) % MOD
        return fact, ifact

    def get_bc(n, k):
        nonlocal MOD, fact, ifact
        return 0 if k > n or k < 0 else fact[n] * ifact[k] % MOD * ifact[n - k] % MOD

    max_n = max(n for n, k in NK)
    fact, ifact = get_fact_n_ifact(max_n)
    results = [str(get_bc(n, k)) for n, k in NK]
    print("\n".join(results))
          
if __name__ == '__main__': boj13977()