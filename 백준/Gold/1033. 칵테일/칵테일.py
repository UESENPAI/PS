import sys
from collections import defaultdict
from math import gcd
from functools import reduce
input = sys.stdin.readline

def boj1033():
    N = int(input().strip())
    ratios = [tuple(map(int, input().strip().split())) for _ in range(N-1)]
    
    graph = defaultdict(list)
    for a, b, p, q in ratios:
        graph[a].append((b, (p, q)))
        graph[b].append((a, (q, p)))
        
    ratio = [(-1, -1)] * N
    def dfs(ratio, node, parent, num, denom):
        nonlocal graph
        ratio[node] = (num, denom)
        for nxt, (p, q) in graph[node]:
            if ratio[nxt] == (-1, -1):
                dfs(ratio, nxt, node, num * q, denom * p)
    dfs(ratio, 0, -1, 1, 1)
        
    num, denom = [num for num, _ in ratio], [denom for _, denom in ratio]

    lcm = lambda a, b: a * b // gcd(a, b)
        
    com_denom = reduce(lcm, denom)
    masses = [n * (com_denom // d) for n, d in ratio]
        
    GCD = reduce(gcd, masses)
    masses = [m // GCD for m in masses]
        
    print(" ".join(map(str, masses)))
    
if __name__ == '__main__': boj1033()