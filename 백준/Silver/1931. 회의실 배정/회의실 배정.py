import sys

N = int(sys.stdin.readline().strip())

mt = []
for _ in range(N): mt.append(list(map(int,sys.stdin.readline().strip().split())))

mt.sort(key=lambda x:(x[1], x[0]))

cnt = 1
end = mt[0][1]

for i in range(1, N):
    if mt[i][0] >= end:
        cnt += 1
        end = mt[i][1]

print(cnt)
