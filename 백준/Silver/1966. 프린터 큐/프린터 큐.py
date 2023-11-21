import sys
from collections import deque

T = int(sys.stdin.readline().strip())

for _ in range(T):
    N, M = map(int, sys.stdin.readline().strip().split())
    pque = deque([_ for _ in range(1, N+1)])
    crt = deque(list(map(int, sys.stdin.readline().strip().split())))

    ans = 0
    while len(pque):
        ready = True
        if len(pque) != 1:
            for num in range(1,len(pque)):
                if crt[0] < crt[num]:
                    crt.append(crt.popleft())
                    pque.append(pque.popleft())
                    ready = False
                    break
        if ready:
            ans+=1
            tmp = pque.popleft()
            if tmp == M+1:
                print(ans)
                continue
            crt.popleft()