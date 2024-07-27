from sys import stdin, stdout
input = stdin.readline

def boj1117():
    W, H, f, c, x1, y1, x2, y2 = map(int, input().split())
    
    x = f if W - f < (W >> 1) else W - f
    dx, dy, n, a = W - x, c + 1, x2 - x1, W * H 
    if x1 < dx:
        if x2 > dx: n += (dx - x1)
        else: n <<= 1
    print(a - (n * (y2 - y1) * dy))

if __name__ == '__main__': boj1117()