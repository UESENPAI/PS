import sys

T = int(sys.stdin.readline().strip())

for _ in range(T):
    stack = list(sys.stdin.readline().strip())

    cnt = 0
    while len(stack):
        t = stack.pop()
        if t==')': cnt+=1
        elif t=='(': cnt-=1
        else: raise ValueError("NANI?")
        
        if cnt < 0:
            break
        
    if not cnt: print("YES")
    else: print("NO")
        