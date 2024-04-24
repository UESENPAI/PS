import sys
input = sys.stdin.readline

def boj19539():
    N = int(input().strip())
    hi = list(map(int, input().strip().split()))
    
    sumh = sum(hi)
    s = 0
    
    if sumh % 3: print("NO")
    else:
        for h in hi: s += h>>1
        print("NO") if s < sumh//3 else print("YES")
                 
if __name__ == '__main__': boj19539()