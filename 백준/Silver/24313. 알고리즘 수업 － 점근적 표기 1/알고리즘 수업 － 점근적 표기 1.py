import sys

a1, a0 = map(int, sys.stdin.readline().strip().split())
c = int(sys.stdin.readline().strip())
n0 = int(sys.stdin.readline().strip())

def f(n):
    global a1, a0
    return a1*n+a0

def g(n):
    return n

def isok():
    global c, n0
    for n in range(n0, 101):
        if f(n)>c*g(n):
            return False
    return True

if isok(): print(1)
else: print(0)