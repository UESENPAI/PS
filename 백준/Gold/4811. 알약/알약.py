import sys
from math import factorial
input = sys.stdin.readline

def boj4811():
    catalan = lambda n: factorial(2 * n) // (factorial(n) * factorial(n + 1))
    while True:
        tc = int(input().strip())
        if not tc: break
        print(catalan(tc))

if __name__ == '__main__': boj4811()