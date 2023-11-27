import sys
input = sys.stdin.readline
from collections import deque

def boj2346(N):
    paper = list(map(int, input().strip().split()))
    dqi = deque([i for i in range(1,N+1)])
    dq = deque(paper)
    ans = []

    ans.append(dqi.popleft())
    pt = dq.popleft()
    while dq:
        if pt > 0:
            dq.rotate(-(pt - 1))
            dqi.rotate(-(pt - 1))
        else:
            dq.rotate(-pt)
            dqi.rotate(-pt)
            
        ans.append(dqi.popleft())
        pt = dq.popleft()
    print(" ".join(map(str, ans)))
    

if __name__ == "__main__":
    N = int(input().strip())
    boj2346(N)
