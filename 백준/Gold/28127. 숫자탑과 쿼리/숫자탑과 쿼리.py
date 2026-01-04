from sys import stdin
input = stdin.readline

def boj22943():
    from math import isqrt, ceil

    Q = int(input().strip())
    F = lambda k, a, d: (k * ((a << 1) + (k - 1) * d)) >> 1
    out = []
    for _ in range(Q):
        a, d, x = map(int, input().split())

        b = (a << 1) - d
        D = b * b + ((d * x) << 3)
        r = isqrt(D)

        num = -b + r
        den = (d << 1)

        k = ceil(num / den)
        if k < 1: k = 1

        while F(k, a, d) < x: k += 1
        while k > 1 and F(k - 1, a, d) >= x: k -= 1

        pos = x - F(k - 1, a, d)
        out.append(f"{k} {pos}")

    print("\n".join(out))

if __name__ == '__main__': boj22943()