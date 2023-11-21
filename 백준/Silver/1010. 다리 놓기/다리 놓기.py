import sys
from math import factorial

def combination(N, K):
    return factorial(N)//(factorial(K)*factorial(N-K))

T = int(sys.stdin.readline().strip())

for _ in range(T):
    N, M = map(int,sys.stdin.readline().split())
    print(combination(M,N))