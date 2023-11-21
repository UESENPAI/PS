import sys

n, m = map(int,sys.stdin.readline().split())

def numcount(N, arg):
    cnt = 0
    while N!=0:
        N = N//arg
        cnt += N
    return cnt

two = numcount(n, 2) - numcount(m, 2) - numcount((n-m), 2)
five = numcount(n, 5) - numcount(m, 5) - numcount((n-m), 5)

print(min(two,five))