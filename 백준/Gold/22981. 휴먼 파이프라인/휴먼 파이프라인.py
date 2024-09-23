import sys
input = sys.stdin.readline

def boj22981():
    n, k = map(int, input().split())
    v = sorted([*map(int, input().split())])
    ans = 1e18
    for i in range(1, n):
        z = v[0] * i + v[i] * (n - i)
        ans = min(ans, k // z + 1 if k % z else k // z)
    print(ans)

if __name__ == "__main__": boj22981()