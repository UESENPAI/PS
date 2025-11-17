from sys import stdin
input = stdin.readline
 
def boj7571():
    N, M = map(int, input().split())

    rows, cols = map(sorted,zip(*[tuple(map(int, input().split())) for _ in range(M)]))

    r_hf, c_hf = rows[M >> 1], cols[M >> 1]

    dist = 0
    for r in rows: dist += abs(r - r_hf)
    for c in cols: dist += abs(c - c_hf)

    print(dist)

if __name__ == '__main__': boj7571()