import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

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

dfs(R)

ans = [0 for _ in range(0, N+1)]
for idx, node in zip(range(1, N+1), path): ans[node] = idx

print(*ans[1:], sep='\n')