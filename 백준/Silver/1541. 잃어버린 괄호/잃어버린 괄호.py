import sys

mlist = (sys.stdin.readline().strip().split('-'))

ans = 0
for idx in range(len(mlist)):
    tmp = list(map(int,mlist[idx].split('+')))
    if idx:
        ans-=sum(tmp)
    else:
        ans+=sum(tmp)
print(ans)
