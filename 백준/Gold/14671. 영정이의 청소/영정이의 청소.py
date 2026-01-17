import sys
input = sys.stdin.readline

def boj14671():
    N, M, K = map(int, input().split())
    seen = [[False, False], [False, False]]

    for _ in range(K):
        x, y = map(int, input().split())
        seen[x & 1][y & 1] = True

    print("YES" if (seen[0][0] and seen[0][1] and seen[1][0] and seen[1][1]) else "NO")

if __name__ == "__main__": boj14671()