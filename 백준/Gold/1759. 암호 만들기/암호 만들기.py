import sys
from itertools import combinations
from collections import Counter
input = sys.stdin.readline

def boj1759():
    L, C = map(int,input().strip().split())
    alpha = sorted(list(map(str,input().strip().split())))

    vow = {'a', 'e', 'i', 'o', 'u'}
    for c in combinations(alpha,L):
        counter = Counter(c)
        vcnt = sum(counter[v] for v in vow)
        if vcnt>0 and L-vcnt>1: print(''.join(c))

if __name__ == "__main__": boj1759()