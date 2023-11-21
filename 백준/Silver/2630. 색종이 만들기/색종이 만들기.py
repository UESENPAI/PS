import sys

N = int(sys.stdin.readline().strip())
confetti = [list(map(int,sys.stdin.readline().strip().split())) for _ in range(N)]

cnt_blue = 0
cnt_white = 0

def reculsive(x, y, N):
    global cnt_blue, cnt_white
    clr = confetti[x][y]
    n = N//2
    for col in range(x, x+N):
        for row in range(y, y+N):
            if clr != confetti[col][row]:
                reculsive(x, y, n)
                reculsive(x+n, y, n)
                reculsive(x, y+n, n)
                reculsive(x+n, y+n, n)
                return
    if clr: cnt_blue+=1
    else: cnt_white+=1
    return

reculsive(0,0,N)
print(f'{cnt_white}\n{cnt_blue}')
    

