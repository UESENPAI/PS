from sys import stdin
input = stdin.readline

def boj22984():
    N = int(input())
    p = list(map(float, input().split()))
    ans = sum(p)
    for i in range(N - 1): ans += p[i] + p[i + 1] -  2 * p[i] * p[i + 1]
    print(ans)

if __name__ == '__main__': boj22984()