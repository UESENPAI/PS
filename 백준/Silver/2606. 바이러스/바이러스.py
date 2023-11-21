import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N = int(input())
graph = [[] for _ in range (N+1)]
isvisited = [False for _ in range (N+1)]

V = int(input())
for _ in range(V):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(s):
    global graph, isvisited
    isvisited[s] = True

    for g in graph[s]:
        if not isvisited[g]: dfs(g)
    return

dfs(1)
print(isvisited.count(True)-1)