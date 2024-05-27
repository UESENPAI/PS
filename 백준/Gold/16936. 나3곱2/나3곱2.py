import sys
from collections import deque
input = sys.stdin.readline

def boj16563():
    N = int(input())
    B = sorted(list(map(int, input().split())))

    for start in B:
        A = deque([start])
        remaining = set(B)
        remaining.remove(start)

        while len(A) < N:
            na3, gob2 = A[-1] // 3, A[-1] << 1
            if not A[-1] % 3 and na3 in remaining:
                A.append(na3)
                remaining.remove(na3)
            elif gob2 in remaining:
                A.append(gob2)
                remaining.remove(gob2)
            else: break

        if len(A) == N: ans = list(A)

    print(" ".join(map(str, ans)))

if __name__ == '__main__': boj16563()