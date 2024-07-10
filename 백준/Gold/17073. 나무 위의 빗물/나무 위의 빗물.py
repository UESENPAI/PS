from sys import stdin
from collections import defaultdict
input = stdin.readline

def boj17073():
    N, W = map(int, input().strip().split())
    UV = [tuple(map(int, input().strip().split())) for _ in range(N - 1)]

    degrees = defaultdict(int)
    leaf = N-1

    for U, V in UV:
        degrees[U] += 1
        degrees[V] += 1

        if U != 1 and degrees[U] == 2: leaf -= 1
        if V != 1 and degrees[V] == 2: leaf -= 1

    print(W/leaf)

if __name__ == '__main__': boj17073()