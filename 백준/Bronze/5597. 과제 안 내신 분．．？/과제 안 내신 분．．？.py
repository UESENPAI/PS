import sys

s = list(range(1,31))

for _ in range(28):
    num = int(input())
    s.remove(num)

print(f'{min(s)}\n{max(s)}')