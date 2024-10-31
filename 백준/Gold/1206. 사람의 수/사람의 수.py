import sys
from math import trunc

input = sys.stdin.readline

def boj1206():
    N = int(input().strip())
    avg = [float(input()) for _ in range(N)]
    o = 0
    
    def check(o):
        for x in avg:
            l,r=0,10*o
            while l<r:
                mid=(l+r)>>1
                if (mid/o)<x: l=mid+1
                else: r=mid
            if trunc((l/o)*1000)/1000!=x: return False
        return True
    
    while o < 1000:
        o+=1
        if check(o): break
    print(o)

if __name__ == "__main__": boj1206()