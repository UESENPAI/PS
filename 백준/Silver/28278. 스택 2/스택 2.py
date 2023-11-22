import sys
input = sys.stdin.readline

N = int(input().strip())

stack = []

for _ in range(N):
    command = (input().rstrip())
    if len(command)<2:command = int(command)
    else: command = list(map(int,command.split()))

    if command == 2: print(stack.pop()) if stack else print(-1)
    elif command == 3: print(len(stack))
    elif command == 4: print(0) if stack else print(1)
    elif command == 5: print(stack[-1]) if stack else print(-1)
    else: stack.append(int(command[1]))
