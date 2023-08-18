import sys
from collections import deque
#input = sys.stdin.readline
sys.setrecursionlimit(44444)

N, M = map(int, input().strip().split())

graph=[]
for i in range(N): graph.append(list(map(int, input())))
#graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[[0 for _ in range(2)] for _ in range(M)] for _ in range(N)]
dc = [-1, 1, 0, 0]
dr = [0, 0, -1, 1]

def bfs():
    global graph, visited, dc, dr
    queue = deque([(0, 0, 0)])
    visited[0][0][0] = 1

    while queue:
        c, r, issledge = queue.popleft()
        if c == N-1 and r == M-1:
            print(visited[c][r][issledge])
            return
        for i in range(4):
            nc, nr = c + dc[i], r + dr[i]
            if nc<0 or nr<0 or nc>=N or nr>=M: continue
            if not visited[nc][nr][issledge]:
                if graph[nc][nr] and not issledge:
                    queue.append([nc, nr, 1])
                    visited[nc][nr][1] = visited[c][r][issledge]+1
                if not graph[nc][nr]:
                    queue.append([nc,nr,issledge])
                    visited[nc][nr][issledge] = visited[c][r][issledge]+1
    print(-1)
    return

bfs()
