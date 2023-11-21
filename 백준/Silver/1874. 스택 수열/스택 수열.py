import sys

n = int(sys.stdin.readline().strip())

seq = []
for _ in range(n): seq.append(int(sys.stdin.readline().strip()))

stack = []
op = []
idx = 1

for s in seq:
    while True:
        if len(stack) and stack[-1]==s:
            op.append("-")
            stack.pop()
            break
        elif idx<=n:
            stack.append(idx)
            op.append("+")
            idx+=1
        else: break

if len(stack): print("NO")
else: list(map(print, op))