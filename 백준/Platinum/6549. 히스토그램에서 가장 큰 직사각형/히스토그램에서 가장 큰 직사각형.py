import sys

while True:
    T = list(map(int, sys.stdin.readline().strip().split()))
    n = T.pop(0)
    if not n: exit()

    ans, stack = 0, []
    for i in range(n):
        while len(stack) and T[stack[-1]] > T[i]:
            tmp = stack.pop()

            if len(stack): width = i - stack[-1] -1
            else: width = i
            ans = max(ans, width*T[tmp])
        stack.append(i)
        
    while len(stack):
        tmp = stack.pop()
        if len(stack): ans = max(ans, (n-stack[-1]-1)*T[tmp])
        else: width = ans = max(ans, n*T[tmp])
    print(ans)