from sys import stdin
input = stdin.readline

def boj2916():
    from math import gcd
    from functools import reduce

    N, K = map(int, input().split())
    angles = list(map(int, input().split()))
    queries = list(map(int, input().split()))
    g = reduce(gcd, angles, 360)
    for q in queries: print("NO") if q % g else print("YES")

if __name__ == '__main__': boj2916()