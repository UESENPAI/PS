import sys
from itertools import combinations
input = sys.stdin.readline

def boj6603():
    while True:
        tc = list(map(int, input().strip().split()))
        if not tc[0]: break

        k, *s = tc
        for c in combinations(s,6): print(' '.join(map(str, c)))
        print()

if __name__ == "__main__": boj6603()