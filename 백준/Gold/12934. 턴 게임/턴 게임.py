from sys import stdin
input = stdin.readline

def boj12934():
    from math import isqrt

    x, y = map(int, input().split())
    T = x + y

    D = 1 + (T << 3)
    r = isqrt(D)
    if r * r != D:
        print(-1)
        return

    if (r - 1) & 1:
        print(-1)
        return

    N = (r - 1) >> 1
    if ((N * (N + 1)) >> 1) != T:
        print(-1)
        return

    if not x:
        print(0)
        return

    max_sum = lambda N, k: ((k * (((N << 1) - k + 1) >> 1)) if (k & 1) else ((k >> 1) * ((N << 1) - k + 1)))

    lo, hi = 0, N
    while lo < hi:
        mid = (lo + hi) >> 1
        if max_sum(N, mid) >= x:
            hi = mid
        else:
            lo = mid + 1

    print(lo)

if __name__ == '__main__': boj12934()