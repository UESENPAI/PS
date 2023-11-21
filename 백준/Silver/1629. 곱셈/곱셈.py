import sys

A, B, C = map(int, sys.stdin.readline().strip().split())

def recursive (a,b,c):
    if b == 1: return a%c
    else:
        tmp = recursive(a, b//2, c)
        if b%2: return (tmp * tmp * a) % c
        else: return (tmp * tmp) % c
          
print(recursive(A,B,C))