import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
from collections import deque

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
for i in range(1, N+1): graph[i].sort(reverse=False)

dfs_isvisited = [False for _ in range(N+1)]
dfs_path=[]
def dfs(R):
    global graph, dfs_isvisitied, dfs_path
    dfs_isvisited[R] = True
    dfs_path.append(R)
    for node in graph[R]:
        if not dfs_isvisited[node]: dfs(node)
    return

bfs_isvisited = [False for _ in range(N+1)]
bfs_path=[]
def bfs(R):
    global graph, bfs_isvisitied, bfs_path
    bfs_isvisited[R] = True
    q = deque([R])
    while q:
        v = q.popleft()
        bfs_path.append(v)
        for g in graph[v]:
            if not bfs_isvisited[g]:
                bfs_isvisited[g]=True
                q.append(g)

dfs(V)
bfs(V)

print(*dfs_path)
print(*bfs_path)