import sys
input = sys.stdin.readline

def boj1022():
    r1, c1, r2, c2 = map(int,input().strip().split())

    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
    hurricane = [[0 for _ in range(c2-c1+1)] for _ in range(r2-r1+1)]
    total = (c2-c1+1) * (r2-r1+1)
    direction, cnt, l = 1, 1, 1
    x, y = 0, 0
    
    while total > 0:
        for _ in range(2):
            for _ in range(l):
                if r1 <= x <= r2 and c1 <= y <= c2:
                    hurricane[x - r1][y - c1] = cnt
                    total -= 1
                    m = cnt
                x += dx[direction]
                y += dy[direction]
                cnt += 1
            direction = (direction-1) % 4
        l += 1
        
    max_len = len(str(m))
    for r in range(r2-r1+1):
        for c in range(c2-c1+1):
            print(str(hurricane[r][c]).rjust(max_len), end=" ")
        print()

def boj1022_timeout():
    r1, c1, r2, c2 = map(int,input().strip().split())

    lim = max(abs(r1), abs(r2), abs(c1), abs(c2))
    world = [[-1] * ((lim<<1)+1) for _ in range((lim<<1)+1)]

    for r in range(r1 + lim, r2 + lim + 1):
        for c in range(c1 + lim, c2 + lim + 1): world[r][c] = 0

    world[lim][lim] = 1
    n = 1
    for col in range(lim+1, (lim<<1)+1):
        j = (n<<1)+1
        tmp = j*j
        world[col][col] = tmp
        world[col][col-j+1] = tmp - (n<<1)
        world[col-j+1][col-j+1] = tmp - (n<<2)
        world[col-j+1][col] = tmp - 6*n
        n+=1
        
        if any(world[col][c] == 0 for c in range(col, col-j, -1)):
            for c in range(col, col-j, -1):
                if not world[col][c]:
                    world[col][c] = world[col][col] - (col - c)

        if any(world[r][col-j+1] == 0 for r in range(col, col-j, -1)):
            for r in range(col, col-j, -1):
                if not world[r][col-j+1]:
                    world[r][col-j+1] = world[col][col-j+1] - (col - r)

        if any(world[col-j+1][c] == 0 for c in range(col-j+1, col)):
            for c in range(col-j+1, col):
                if not world[col-j+1][c]:
                    world[col-j+1][c] = world[col-j+1][col-j+1] - (c - (col - j + 1))

        if any(world[r][col] == 0 for r in range(col-j+2, col)):
            for r in range(col-j+2, col):
                if not world[r][col]:
                    world[r][col] = world[col-j+1][col] - (r - (col-j+1))

    max_length = max(len(str(num)) for row in world for num in row)

    for r in range(r1 + lim, r2 + lim + 1):
        for c in range(c1 + lim, c2 + lim + 1):
            num = world[r][c]
            if num == -1: print(' ' * max_length, end=' ')
            else: print(str(num).rjust(max_length), end=' ')
        print()

if __name__ == '__main__': boj1022()