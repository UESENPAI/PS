import sys

N = int(sys.stdin.readline().strip())

tr = list()
for _ in range(N): tr.append(list(map(int,sys.stdin.readline().strip().split())))

ans = tr[0][0]
for vt in range(1,N):
    for hz in range(vt+1):
        if hz == 0:
            tr[vt][hz] += tr[vt-1][hz]
        elif hz == vt:
            tr[vt][hz] += tr[vt-1][hz-1]
        else:
             tr[vt][hz] += max([tr[vt-1][hz-1], tr[vt-1][hz]])
        if vt == N-1:
            ans = max(ans,tr[vt][hz])

print(ans)
