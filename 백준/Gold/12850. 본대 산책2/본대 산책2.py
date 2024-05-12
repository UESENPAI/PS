import sys
input = sys.stdin.readline

def boj12850():
    D = int(input().strip())
    mod = 1000000007
    N = 8

    graph = [
    [0, 1, 0, 0, 0, 1, 0, 0],  # 정보과학관
    [1, 0, 1, 0, 0, 0, 1, 0],  # 전산관
    [0, 1, 0, 1, 0, 0, 1, 1],  # 미래관
    [0, 0, 1, 0, 1, 0, 0, 1],  # 신양관
    [0, 0, 0, 1, 0, 0, 0, 1],  # 학생회관
    [1, 0, 0, 0, 0, 0, 1, 0],  # 형남공학관
    [0, 1, 1, 0, 0, 1, 0, 1],  # 진리관
    [0, 0, 1, 1, 1, 0, 1, 0]   # 정문
    ]

    ans = [[1 if i == j else 0 for j in range(8)] for i in range(8)]

    def matmul(A, B, mod=1000000007):
        C = [[0] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                C[i][j] = sum(A[i][k] * B[k][j] for k in range(N)) % mod
        return C

    while D > 0:
        if D & 1: ans = matmul(ans, graph)
        graph = matmul(graph, graph)
        D >>= 1

    print(ans[4][4]) 

if __name__ == '__main__': boj12850()