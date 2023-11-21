import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N = int(input())
graph = [list(map(int, input().strip())) for _ in range(N)]


dx = [-1,1,0,0]
dy = [0,0,-1,1]

cnt = 0
def dfs(x, y):
    if x<0 or x>=N or y<0 or y>=N: return False
    if graph[x][y]:
        graph[x][y]=0
        global cnt
        cnt+=1
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            dfs(nx, ny)
        return True
    return False

ans=0
num=[]
for i in range(N):
    for j in range(N):
        if dfs(i,j):
            num.append(cnt)
            ans+=1
            cnt=0

print(ans)
num.sort(reverse=False)
for n in num: print(n)
