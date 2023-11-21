import sys

arr = ['' for _ in range(15)]
for idx in range(1,6):
    s = sys.stdin.readline().strip()
    for e in range(len(s)):
        arr[e] = arr[e]+s[e]

print(''.join(map(str,[*arr])))