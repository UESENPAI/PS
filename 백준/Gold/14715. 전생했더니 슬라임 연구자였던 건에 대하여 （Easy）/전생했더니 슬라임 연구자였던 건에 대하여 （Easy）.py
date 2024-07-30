from sys import stdin, stdout
from math import isqrt, ceil, log2
input = stdin.readline

def boj14715():
    K = int(input().strip())
    leafs = 1

    while True:
        is_prime = True
        for i in range(2, isqrt(K) + 1):
            if not K % i:
                is_prime = False
                K //= i
                leafs += 1
                break
        if is_prime: break

    print(ceil(log2(leafs)))

if __name__ == '__main__': boj14715()