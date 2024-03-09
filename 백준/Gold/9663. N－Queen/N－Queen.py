import sys
input = sys.stdin.readline

def boj9663():
    N = int(input())
    answer = 0
    column = [False] * N
    diag1 = [False] * (2 * N - 1)
    diag2 = [False] * (2 * N - 1)
    
    def dfs(x):
        nonlocal answer
        if x == N:
            answer += 1
            return
        for y in range(N):
            if not (column[y] or diag1[x + y] or diag2[x - y + N - 1]):
                column[y] = diag1[x + y] = diag2[x - y + N - 1] = True
                dfs(x + 1)
                column[y] = diag1[x + y] = diag2[x - y + N - 1] = False
                
    dfs(0)
    print(answer)

if __name__ == '__main__': boj9663()