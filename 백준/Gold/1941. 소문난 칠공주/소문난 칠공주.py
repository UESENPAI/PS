import sys
from collections import deque
input = sys.stdin.readline

def boj1941():
    graph = [list(input().strip()) for _ in range(5)]

    def unionfind(path):
        parent = [i for i in range(25)]
        
        def find(x):
            nonlocal parent
            if parent[x] != x: parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            nonlocal parent
            a, b = find(a), find(b)
            if a < b: parent[b] = a
            else: parent[a] = b
        
        for n in path:
            x, y = n // 5, n % 5
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < 5 and 0 <= ny < 5 and (nx * 5 + ny) in path: union(n, nx * 5 + ny)

        root = find(path[0])
        for p in path[1:]:
            if find(p) != root: return False
        return True

    def dfs(n, path):
        nonlocal graph, ans
        if len(path) > 7: return

        if n == 25:
            if len(path) == 7 and sum(1 for i in path if graph[i // 5][i % 5] == 'S') >= 4:
                if unionfind(path): ans.append(path[:])
            return
        dfs(n + 1, path + [n])
        dfs(n + 1, path)
        
    
    ans = []
    isvisited = [[False]*5 for _ in range(5)]
    dfs(0, [])
    print(len(ans))

if __name__ == '__main__': boj1941()
