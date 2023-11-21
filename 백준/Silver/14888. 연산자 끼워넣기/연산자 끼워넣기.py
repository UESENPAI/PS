import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
op = list(map(int, sys.stdin.readline().split()))

maximum = -1e9
minimum = 1e9

def cpp14div(arg1, arg2):
    if arg1*arg2<0:
        return -(abs(arg1)//abs(arg2))
    else:
        return abs(arg1)//abs(arg2)

def dfs(idx, total, plus, minus, multiply, divide):
    global maximum, minimum
    if idx == N:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return

    if plus:
        dfs(idx + 1, total + A[idx], plus - 1, minus, multiply, divide)
    if minus:
        dfs(idx + 1, total - A[idx], plus, minus - 1, multiply, divide)
    if multiply:
        dfs(idx + 1, total * A[idx], plus, minus, multiply - 1, divide)
    if divide:
        dfs(idx + 1, cpp14div(total, A[idx]), plus, minus, multiply, divide - 1)


dfs(1, A[0], op[0], op[1], op[2], op[3])

print(f'{maximum}\n{minimum}')
