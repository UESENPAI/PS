import sys
from math import factorial

N, K = map(int,sys.stdin.readline().split())

def combination(N, K):
    return factorial(N)//(factorial(K)*factorial(N-K))

print(combination(N,K))