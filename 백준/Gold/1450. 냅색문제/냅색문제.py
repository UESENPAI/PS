import sys
from itertools import combinations
input = sys.stdin.readline



def boj1450_DP():
    N, C = map(int, input().strip().split())
    W = list(map(int, input().strip().split()))

    dp = [[0] * (C + 1) for _ in range(N + 1)]

    ans = 0

    def dfs(idx, subsum):
        nonlocal ans, N, C, W
        if subsum > C or idx > N: return

        if idx == N:
            ans += 1
            return

        dfs(idx + 1, subsum + W[idx])
        dfs(idx + 1, subsum)

    dfs(0, 0)
    print(ans)



def boj1450_MITM():
    N, C = map(int, input().strip().split())
    W = list(map(int, input().strip().split()))
    WF, WL = W[:N//2], W[N//2:]

    SWF = sorted([sum(comb) for i in range(N//2 + 1) for comb in combinations(WF, i)])
    SWL = [sum(comb) for i in range(N//2 + 2) for comb in combinations(WL, i)]
    ans = 0

    for swl in SWL:
        if swl > C: continue
        fp, lp = 0, len(SWF)-1
        while fp<=lp:
            mp = (fp+lp)//2
            if SWF[mp]+swl>C: lp = mp -1
            else: fp = mp + 1
        ans += lp +1

    print(ans)



if __name__ == "__main__": 
    #boj1450_DP()
    boj1450_MITM()