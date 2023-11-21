import sys

N = int(sys.stdin.readline().strip())

stack=[]
for _ in range(N):
    arg = sys.stdin.readline().strip().split()

    if arg[0]=="push":
        stack.append(int(arg[1]))
    elif arg[0]=="pop":
        if len(stack):
            print(stack[-1])
            stack.pop()
        else: print(-1)
    elif arg[0]=="size":
        print(len(stack))
    elif arg[0]=="empty":
        if not len(stack): print(1)
        else: print(0)
    elif arg[0]=="top":
        if len(stack): print(stack[-1])
        else: print(-1)
    else:
        raise Exception("NANI?!")