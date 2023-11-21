import sys
from math import lcm
from math import gcd

A1, B1 = map(int, sys.stdin.readline().strip().split())
A2, B2 = map(int, sys.stdin.readline().strip().split())
B=lcm(B1,B2)
b1 = B//B1
b2 = B//B2
C = A1*b1 + A2*b2
d=gcd(C, B)
dC = C//d
dB = B//d

print(f'{dC} {dB}')
