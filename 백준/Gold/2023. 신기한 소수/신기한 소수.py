import sys
from math import sqrt

input = sys.stdin.readline

def boj2023():
    N = int(input().strip())

    def is_prime(num):
        for div in range(2, int(sqrt(num)) + 1):
            if not num % div: return False
        return True

    def solve(num):
        if len(str(num)) == N:
            if is_prime(num): print(num)
            return

        for i in range(10):
            k = num * 10 + i
            if is_prime(k): solve(k)

    for i in [2, 3, 5, 7]: solve(i)

if __name__ == '__main__': boj2023()