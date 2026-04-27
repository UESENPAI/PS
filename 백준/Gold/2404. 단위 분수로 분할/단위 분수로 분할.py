from sys import stdin
input = stdin.readline


def boj2404():
    from math import gcd
    from functools import lru_cache

    p, q, a, n = map(int, input().split())

    g = gcd(p, q)
    p //= g
    q //= g

    @lru_cache(None)
    def dfs(num, den, min_d, left, limit):
        if num == 0: return 1

        if left == 0: return 0

        if limit < min_d: return 0

        if num * min_d > den * left: return 0

        lo = max(min_d, (den + num - 1) // num)

        hi = min(limit, (left * den) // num)

        ans = 0

        for d in range(lo, hi + 1):
            next_num = num * d - den
            next_den = den * d

            g = gcd(next_num, next_den)
            next_num //= g
            next_den //= g

            ans += dfs(next_num, next_den, d, left - 1, limit // d)

        return ans

    print(dfs(p, q, 1, n, a))

if __name__ == "__main__": boj2404()