from sys import stdin, stdout, setrecursionlimit
from math import gcd
input = stdin.readline
setrecursionlimit(10**6)
 
def boj21870():
    N = int(input().strip())
    a = list(map(int, input().strip().split()))

    def gcds(a):
        c = a[0]
        for b in a[1:]: c = gcd(c, b)
        return c

    def dnc(a):
        if len(a) < 3: return sum(a)
        else:
            mid = len(a)>>1
            l, r = dnc(a[:mid]) + gcds(a[mid:]), dnc(a[mid:]) + gcds(a[:mid])
            return max(l, r)

    mid = N>>1
    print(a[0]) if (N < 2) else print(max(dnc(a[:mid]) + gcds(a[mid:]), dnc(a[mid:]) + gcds(a[:mid])))

if __name__ == '__main__': boj21870()