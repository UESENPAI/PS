import sys

num = []

for i in range(5):
    num.append(int(sys.stdin.readline()))

num.sort()

print(f'{sum(num) // 5}\n{num[2]}')