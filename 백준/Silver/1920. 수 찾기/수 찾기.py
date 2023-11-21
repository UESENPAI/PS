import sys

N = int(sys.stdin.readline().strip())

A=set(map(int, sys.stdin.readline().strip().split()))

M = int(sys.stdin.readline().strip())

X=list(map(int, sys.stdin.readline().strip().split()))

for x in X: print(1) if x in A else print(0)