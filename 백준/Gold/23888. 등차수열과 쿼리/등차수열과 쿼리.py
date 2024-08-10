from sys import stdin, stdout
from math import gcd
input = stdin.readline

def boj23888():
    a, d = map(int, input().strip().split())
    q = int(input().strip())
    qs = [tuple(map(int, input().strip().split())) for _ in range(q)]
    
    for t,l,r in qs:
        if t == 1:
            al, ar, n = a + (l - 1) * d, a + (r - 1) * d, r - l + 1
            sigma = (n * (al + ar))>>1
        elif t == 2:
            if l == r: sigma = a + (r-1) * d
            else: sigma = gcd(a + (l - 1) * d, d) if d else (a + (l - 1) * d)
        print(sigma)

if __name__ == '__main__': boj23888()