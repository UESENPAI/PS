import sys
from math import lcm

T = int(sys.stdin.readline().strip())

for _ in range (T):
    A, B = map(int,sys.stdin.readline().split())
    print(f'{lcm(A,B)}')
    