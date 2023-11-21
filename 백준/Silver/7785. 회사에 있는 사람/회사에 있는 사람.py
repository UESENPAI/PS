import sys

n = int(sys.stdin.readline().strip())

ans = set()
for _ in range(n):
    arg = sys.stdin.readline().strip().split()
    if arg[1] == "enter": ans.add(arg[0])
    elif arg[1] == "leave": ans.remove(arg[0])

ans=list(ans)
ans.sort(reverse=True)
[*map(lambda x: print(*x), zip(ans))]