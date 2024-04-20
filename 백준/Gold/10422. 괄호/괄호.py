import sys
from math import factorial
input = sys.stdin.readline

def boj10422():
    T = int(input().strip())
    L = [int(input().strip()) for _ in range(T)]
    div = 1000000007

    catalan = lambda n: factorial(n << 1) // (factorial(n) * factorial(n + 1))

    for l in L: print(catalan(l>>1)%div) if not l%2 else print(0)
                 
if __name__ == '__main__': boj10422()