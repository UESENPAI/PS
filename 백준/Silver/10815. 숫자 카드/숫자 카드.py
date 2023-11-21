import sys

N = int(sys.stdin.readline())

cardnums = set(map(int,sys.stdin.readline().split()))

M = int(sys.stdin.readline())

isown = list(map(int,sys.stdin.readline().split()))

cardown = cardnums.intersection(cardnums, set(isown))

ans = []

for e in isown:
    if e in cardown:
        ans.append('1')
    else:
        ans.append('0')
    ans.append(' ')

print(''.join(ans))