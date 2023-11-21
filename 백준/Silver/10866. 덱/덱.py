import sys
from collections import deque

N = int(sys.stdin.readline().strip())

dp = deque([])
for _ in range(N):
    arg = sys.stdin.readline().strip().split()

    if arg[0]=="push_front":
        dp.appendleft(arg[1])
    elif arg[0]=="push_back":
        dp.append(arg[1])
    elif arg[0]=="pop_front":
        if len(dp): print(dp.popleft())
        else: print(-1)
    elif arg[0]=="pop_back":
        if len(dp): print(dp.pop())
        else: print(-1)
    elif arg[0]=="size":
        print(len(dp))
    elif arg[0]=="empty":
        if len(dp): print(0)
        else: print(1)
    elif arg[0]=="front":
        if len(dp): print(dp[0])
        else: print(-1)
    elif arg[0]=="back":
        if len(dp): print(dp[-1])
        else: print(-1)