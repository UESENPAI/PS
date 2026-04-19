from sys import stdin
input = stdin.readline

def boj27297():
    N, M = map(int, input().split())
    points = [list(map(int, input().split())) for _ in range(M)]
    
    F = []
    
    for j in range(N):
        coord = [points[i][j] for i in range(M)]
        coord.sort()
        F.append(coord[M // 2])
    
    total = 0
    for i in range(M):
        for j in range(N):
            total += abs(points[i][j] - F[j])
    
    print(total)
    print(*F)

if __name__ == "__main__": boj27297()