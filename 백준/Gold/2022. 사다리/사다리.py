import sys
input = sys.stdin.readline

def boj2022():
    x, y, c = map(float, input().strip().split())
    high, low = min(x,y), 1
    ans = 0
    while low+0.001 <= high:
        w = (low+high)/2
        h1, h2 = (x**2-w**2)**0.5, (y**2-w**2)**0.5
        c_ = (h1*h2)/(h1+h2)
        if c_ < c: high = w
        else: ans, low = w, w
    print(f"{round(ans, 3):.3f}")
                 
if __name__ == '__main__': boj2022()