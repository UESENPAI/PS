import sys
input = sys.stdin.readline

def boj10253():
    N, K, M = map(int,input().strip().split())

    def modular_exponentiation(base, exp, mod):
        result = 1
        while exp > 0:
            if exp % 2 == 1:
                result *= base
                result %= mod
            base **= 2
            base %= mod
            exp >>= 1
        return result

    def modular_inverse(base, mod): return modular_exponentiation(base, mod - 2, mod)

    def binomial_mod(n, k, mod):
        if k > n: return 0
        numerator, denominator = 1, 1
        for i in range(k):
            numerator *= n - i
            numerator %= mod
            denominator *= (i + 1)
            denominator %= mod
        return (numerator * modular_inverse(denominator, mod)) % mod

    def decimal_to_base(n, m):
        digits = []
        while n > 0:
            digits.append(n % m)
            n //= m
        return digits

    def lucas_theorem(n, k, m):
        n_digits, k_digits = decimal_to_base(n, m), decimal_to_base(k, m)
        k_digits += [0] * (len(n_digits) - len(k_digits))
        result = 1
        for ni, ki in zip(n_digits, k_digits):
            result *= binomial_mod(ni, ki, m)
            result %= m
        return result

    result = lucas_theorem(N, K, M)
    print(result)

if __name__ == '__main__': boj10253()