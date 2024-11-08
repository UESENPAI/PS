import sys
input = sys.stdin.readline

def boj11054():
    N = int(input().strip())
    S = list(map(int, input().strip().split()))
    rS = S[::-1]

    dpS, dprS = [1 for _ in range(N)], [1 for _ in range(N)]
    for i in range(N):
        for j in range(i):
            if S[i]>S[j]: dpS[i] = max(dpS[i],dpS[j]+1)
            if rS[i]>rS[j]: dprS[i] = max(dprS[i],dprS[j]+1)

    result = [0 for _ in range(N)]
    for i in range(N): result[i] = dpS[i] + dprS[(N-1)-i] -1

    print(max(result))

if __name__ == "__main__": boj11054()