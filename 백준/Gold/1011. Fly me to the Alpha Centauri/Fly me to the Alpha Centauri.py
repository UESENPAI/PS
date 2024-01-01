import sys
from math import sqrt, floor

input = sys.stdin.readline

def boj1011():
    T = int(input())
    for _ in range(T):
        x, y = map(int, input().strip().split())
        n = y-x
        r = sqrt(y-x)

        ans = 0
        if floor(r)**2 == n: ans = 2*int(r)-1
        else:
            if int(r)**2+int(r)>=n: ans = 2 * int(r)
            else: ans = 2 * int(r) + 1
        print(ans)

if __name__ == "__main__": boj1011()