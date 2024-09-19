import sys
from math import gcd
from collections import defaultdict
input = sys.stdin.readline

def boj20157():
    N = int(input().strip())
    coords = list(tuple(map(int, input().strip().split())) for _ in range(N))

    slope = defaultdict(int)
    for x, y in coords:
        if not (x | y): continue
        elif not x: slope[(0, -1 if y < 0 else 1)] += 1
        elif not y: slope[(-1 if x < 0 else 1, 0)] += 1
        else:
            _gcd = gcd(x, y)
            x //= _gcd
            y //= _gcd
            slope[(x, y)] += 1

    ans = max(slope.values())
    print(ans)

if __name__ == "__main__": boj20157()