import sys
input = sys.stdin.readline

def boj2580():
    graph = [list(map(int, input().strip().split())) for _ in range(9)]

    blank = [(i, j) for i in range(9) for j in range(9) if not graph[i][j]]

    def checkLine(idx, a, isrow=True):
        for i in range(9):
            if a == (graph[idx][i] if isrow else graph[i][idx]): return False
        return True

    def checkRect(x, y, a):
        nx, ny = x // 3 * 3, y // 3 * 3
        for i in range(3):
            for j in range(3):
                if a == graph[nx+i][ny+j]: return False
        return True


    def dfs(idx):
        if idx == len(blank):
            list(map(lambda row: print(*row), graph))
            exit()

        for i in range(1, 10):
            x, y = blank[idx][0], blank[idx][1]
            if checkLine(x, i, True) and checkLine(y, i, False) and checkRect(x, y, i):
                graph[x][y] = i
                dfs(idx+1)
                graph[x][y] = 0
                
    dfs(0)

if __name__ == "__main__": boj2580()