from sys import stdin
from math import gcd
from functools import reduce
input = stdin.readline

def boj16400():
    n = int(input())
    Ns = list(map(int, input().split()))
    
    diff = [abs(Ns[i] - Ns[0]) for i in range(1, n)]
    result = reduce(gcd, diff)
    print(result)

if __name__ == '__main__': boj16400()