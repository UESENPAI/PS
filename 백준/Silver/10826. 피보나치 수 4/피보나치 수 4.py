import sys
from functools import lru_cache
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def boj10826():
    n = int(input().strip())

    @lru_cache
    def fib(n): return n if n<2 and n>-1 else (fib(n-1) + fib(n-2))

    print(fib(n))

if __name__ == "__main__": boj10826()
 

