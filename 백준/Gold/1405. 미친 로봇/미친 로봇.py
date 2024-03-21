import sys
input = sys.stdin.readline

def boj1405():
    inputs = list(map(int, input().strip().split()))
    for d in range(1, 5): inputs[d]/=100

    dx, dy = [1, -1 ,0, 0], [0, 0, 1, -1]
    
    def dfs(x, y, steps, prob):
        nonlocal isvisited, inputs, ans
        if steps == inputs[0]:
            ans+=prob
            return
        isvisited[x][y] = True
        xub, yub = (inputs[0]<<1), (inputs[0]<<1)
        for d in range(4):
            nxtx, nxty = x+dx[d], y+dy[d]
            if (nxtx < 0) or (nxty<0) or (nxtx > xub) or (nxty > yub): continue
            if isvisited[nxtx][nxty]: continue
            dfs(nxtx, nxty, steps+1, prob*inputs[d+1])
            isvisited[nxtx][nxty] = False

    isvisited = [[False] * ((inputs[0]<<1) + 1) for _ in range(((inputs[0]<<1) + 1))]
    isvisited[inputs[0]][inputs[0]] = True
    ans = 0
    dfs(inputs[0], inputs[0], 0, 1)

    print(ans)

if __name__ == '__main__': boj1405()