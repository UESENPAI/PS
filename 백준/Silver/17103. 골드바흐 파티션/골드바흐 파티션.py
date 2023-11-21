import sys

T = int(sys.stdin.readline().strip())
Ns = []
for _ in range(T): Ns.append(int(sys.stdin.readline().strip()))

memo = [True for _ in range(max(Ns)+1)]
memo[0], memo[1] = False, False

end = max(Ns)
for idx in range(2, (end//2 + 1)):
    if memo[idx]:
        for m in range(idx+idx, end+1, idx):
            memo[m]=False

for N in Ns:
    gp=0
    end = N//2+1
    for i in range(2, end):
        if memo[i]*memo[N-i]: gp +=1
    print(gp)
