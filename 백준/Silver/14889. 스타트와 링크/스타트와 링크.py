import sys

N = int(sys.stdin.readline())

S = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

def getdiff(team1, team2):
    global S
    teamsum1 = 0
    teamsum2 = 0
    for i in range(N//2-1):
        for j in range(i+1, N//2):
            teamsum1 += S[team1[i]][team1[j]] + S[team1[j]][team1[i]]
            teamsum2 += S[team2[i]][team2[j]] + S[team2[j]][team2[i]]
    return abs(teamsum1-teamsum2)
        

def dfs(depth, idx):
    global minimum, isvisited, start, link

    if depth == N/2:
        for n in range(N):
            if n not in start:
                link.append(n)        
        minimum = min(minimum, getdiff(start, link))
        link.clear()
        return

    for i in range(idx,N):
        if not isvisited[i]:
            isvisited[i] = True
            start.append(i)
            dfs(depth+1, i+1)
            #print(f'{start}\n')
            start.pop()
            isvisited[i] = False

start, link = [], []
isvisited = [False for _ in range(N)]
minimum = 1e4
dfs(0, 0)
print(minimum)
