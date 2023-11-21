import sys

N = int(sys.stdin.readline().strip())

que=[]
idx = 0
for _ in range(N):
    arg = sys.stdin.readline().strip().split()

    if arg[0]=="push":
        que.append(int(arg[1]))
    elif arg[0]=="pop":
        if len(que) > idx:
            print(que[idx])
            idx+=1
        else: print(-1)
    elif arg[0]=="size":
        print(len(que)-idx)
    elif arg[0]=="empty":
        if len(que) == idx : print(1)
        else: print(0)
    elif arg[0]=="front":
        if len(que)>idx : print(que[idx])
        else: print(-1)
    elif arg[0]=="back":
        if len(que)>idx: print(que[-1])
        else: print(-1)