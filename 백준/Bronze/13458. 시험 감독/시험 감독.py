import sys
from math import ceil
input = sys.stdin.readline

def boj13458():
    N = int(input().strip())
    Ai = list(map(int, input().strip().split()))
    B, C = map(int, input().strip().split())

    ans = 0
    for a in Ai:
        ans += 1
        if a - B > 0: ans+= ceil((a-B)/C)
    print(ans)

if __name__ == "__main__": boj13458()