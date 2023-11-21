import sys
from collections import deque

N, M = map(int,sys.stdin.readline().strip().split())
a = deque([_ for _ in range(1, N+1)])

target = list(map(int,sys.stdin.readline().strip().split()))

ans = 0
for idx in range(M):
    if a[0] == target[idx]:
        a.popleft()
        continue
    else:
        c2, c3 = 0, 0
        while True:
            if a[c3]==target[idx]:
                for _ in range(c3):
                    if len(a): a.append(a.popleft())
                ans+=c3
                break
            elif a[c2]==target[idx]:
                for _ in range(abs(c2)):
                    if len(a): a.appendleft(a.pop())
                ans+=abs(c2)
                break
            c2-=1
            c3+=1

        assert a[0] == target[idx]
        a.popleft()

print(ans)