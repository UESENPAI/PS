import sys
from math import sqrt
input = sys.stdin.readline

def boj1669():
    X, Y = map(int, input().split())
    if X == Y: print(0)
    else:
        diff = Y-X
        rs = int(sqrt(diff))
        rs2 = rs<<1
        if rs*rs == diff: print(rs2-1)
        else:
            rem = diff - rs*rs
            print(rs2+1) if rem>rs else print(rs2)

if __name__ == '__main__': boj1669()