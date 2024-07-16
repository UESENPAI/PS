from sys import stdin
from math import sqrt
input = stdin.readline

def boj1557():
    k = int(input().strip())
    UBOUND = 1000000000

    def func_mobius(n):
        if n == 1: return 1
        p = 0
        for i in range(2, int(sqrt(n)) + 1):
            if not n % (i * i): return 0
            if not n % i:
                p += 1
                n //= i
                while not n % i:
                    n //= i
        if n > 1: p += 1
        return -1 if p % 2 else 1

    def get_mobius(n):
        mobius = [1] * (n + 1)
        
        for i in range(2, n + 1):
            if mobius[i] == 1:
                for j in range(i, n + 1, i): mobius[j] *= -i
                for j in range(i * i, n + 1, i * i): mobius[j] = 0
        for i in range(2, n + 1):
            if mobius[i] == i: mobius[i] = 1
            elif mobius[i] == -i: mobius[i] = -1
            elif mobius[i] < 0: mobius[i] = 1
            elif mobius[i] > 0: mobius[i] = -1
        return mobius

    mobius = get_mobius(1000000)

    def square_no_no(n):
        nonlocal mobius
        p = 0
        for i in range(1, int(sqrt(n)) + 1):
            p += mobius[i] * (n // (i * i))
        return p
    
    l, r = 0, UBOUND<<1
    while l < r - 1:
        mid = (l + r) >> 1
        if square_no_no(mid) < k: l = mid
        else: r = mid
    print(r)

if __name__ == '__main__': boj1557()