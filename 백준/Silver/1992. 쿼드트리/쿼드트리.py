import sys

N = int(sys.stdin.readline().strip())
pxr = [sys.stdin.readline().strip() for _ in range(N)]
pxr = list(map(lambda x: list(map(int, x)), zip(*pxr)))

def quadtree(x, y, N):
    global comp
    iswhite = pxr[x][y]
    n = N//2
    for col in range(x, x+N):
        for row in range(y, y+N):
            if iswhite != pxr[col][row]:
                print("(", end='')
                quadtree(x, y, n)
                quadtree(x+n, y, n)
                quadtree(x, y+n, n)
                quadtree(x+n, y+n, n)
                print(")", end='')
                return
    if iswhite: print(1, end='')
    else: print(0, end='')
    return

quadtree(0,0,N)