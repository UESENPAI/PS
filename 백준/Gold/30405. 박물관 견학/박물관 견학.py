from sys import stdin
input = stdin.readline

def boj30405():
    N, M = map(int, input().split())

    points = []

    for _ in range(N):
        data = list(map(int, input().split()))
        k = data[0]
        p = data[1:]
        
        points.append(p[0])
        points.append(p[-1])

    points.sort()

    print(points[N - 1])

if __name__ == '__main__': boj30405()