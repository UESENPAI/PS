import sys
input = sys.stdin.readline

def boj20444():
    n, k = map(int,input().strip().split())
    l, r = 0, n>>1
    
    ans = False
    while not l > r:
        v = (l+r)>>1
        h = n - v
        p = (v+1)*(h+1)

        if k>p: l=v+1
        elif k<p: r=v-1
        else:
            ans = True
            break
    print("YES") if ans else print("NO")

if __name__ == '__main__': boj20444()