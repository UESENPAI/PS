import sys

K = int(sys.stdin.readline().strip())

stack=[]
for _ in range(K):
    k = (int(sys.stdin.readline().strip()))
    if k: stack.append(k)
    else:stack.pop()

print(sum(stack))
