import sys

N = int(sys.stdin.readline().strip())

S=[]
S=list(map(int,sys.stdin.readline().strip().split()))

rS = S[::-1]

dpS, dprS = [1 for _ in range(N)], [1 for _ in range(N)]
for i in range(N): #LIS 
    for j in range(i):
        if S[i]>S[j]: dpS[i] = max(dpS[i],dpS[j]+1)
        if rS[i]>rS[j]: dprS[i] = max(dprS[i],dprS[j]+1)

result = [0 for _ in range(N)]
for i in range(N): result[i] = dpS[i] + dprS[(N-1)-i] -1

print(max(result))