import sys
input = sys.stdin.readline
from collections import deque

def boj17471():
    N = int(input().strip())
    weights = list(map(int,input().strip().split()))
    graph = [list(map(lambda x: int(x) - 1, input().strip().split()[1:])) for _ in range(N)]

    def bfs(g):
        nonlocal N, weights, graph
        
        q = deque()
        isvisited = [False for _ in range(N)]
        q.append(g[0])
        isvisited[g[0]] = True

        cnt, buffer = 1, 0
        while q:
            ptr = q.popleft()
            buffer += weights[ptr]
            for nptr in graph[ptr]:
                if nptr in g and not isvisited[nptr]:
                    isvisited[nptr] = True
                    cnt+=1
                    q.append(nptr)

        return buffer if cnt == len(g) else False


    def dfs(cnt, x, end):
        nonlocal mval, isvisited
        
        if cnt == end:
            g1, g2 = deque(), deque()
            for nptr in range(N): g1.append(nptr) if isvisited[nptr] else g2.append(nptr)
                    
            ans1, ans2 = bfs(g1), bfs(g2)
            if not ans1 or not ans2: return
            mval = min(mval, abs(ans1-ans2))
            return
        
        for i in range(x, N):
            if isvisited[i]: continue
            isvisited[i] = True
            dfs(cnt+1, i, end)
            isvisited[i] = False


    mval = sys.maxsize
    for case in range(1, (N>>1) + 1):
        isvisited = [False for _ in range(N)]
        dfs(0, 0, case)


    print(-1) if mval == sys.maxsize else print(mval)
    
if __name__ == '__main__': boj17471()
