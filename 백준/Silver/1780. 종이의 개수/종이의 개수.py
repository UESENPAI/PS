import sys

N = int(sys.stdin.readline().strip())
confetti = [list(map(int,sys.stdin.readline().strip().split())) for _ in range(N)]

cnt = [0, 0, 0]

def recursive(x, y, N):
    global cnt
    clr = confetti[x][y]
    n = N//3
    for col in range(x, x+N):
        for row in range(y, y+N):
            if clr != confetti[col][row]:
                recursive(x, y, n)
                recursive(x+n, y, n)
                recursive(x+2*n, y, n)
                recursive(x, y+n, n)
                recursive(x+n, y+n, n)
                recursive(x+2*n, y+n, n)
                recursive(x, y+2*n, n)
                recursive(x+n, y+2*n, n)
                recursive(x+2*n, y+2*n, n)
                return
    if clr==-1: cnt[0]+=1
    elif not clr: cnt[1]+=1
    elif clr==1: cnt[2]+=1
    else: raise ValueError(clr)
    return

recursive(0,0,N)
print('\n'.join(str(_) for _ in cnt))