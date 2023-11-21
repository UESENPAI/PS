import sys

N = int(sys.stdin.readline().strip())

def factorial(N):
    if not N: return 1
    return N * factorial(N-1)

print(factorial(N))