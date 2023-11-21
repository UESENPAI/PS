import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
from collections import deque

N, M, R = map(int, input().split())
visited = [0 for _ in range(N+1)]
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
for i in range(1, N+1): graph[i].sort(reverse=True)

path=[]
def dfs(R):
    global graph, visitied, path
    visited[R] = 1
    path.append(R)
    for node in graph[R]:
        if not visited[node]: dfs(node)
    return

cnt = 1
def bfs(R):
    global graph, visitied, cnt
    visited[R] = 1
    q = deque([R])
    while q:
        v = q.popleft()
        graph[v].sort(reverse=False)
        for g in graph[v]:
            if not visited[g]:
                cnt+=1
                visited[g]=cnt
                q.append(g)
    
'''
dfs(R)
ans = [0 for _ in range(0, N+1)]
for idx, node in zip(range(1, N+1), path): ans[node] = idx
print(*ans[1:], sep='\n')
'''

bfs(R)
for v in visited[1:]: print(v)