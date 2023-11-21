import sys

N = int(sys.stdin.readline().strip())

wt = (list(map(int,sys.stdin.readline().strip().split())))
wt.sort()
ans = 0
for idx, time in enumerate(wt):
    ans+=(N-idx)*time
print(ans)
