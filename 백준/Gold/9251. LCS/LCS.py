import sys

S1 = (sys.stdin.readline().strip())
S2 = (sys.stdin.readline().strip())
LCS = [[0 for _ in range(len(S2)+1)] for _ in range(len(S1)+1)]

for s1 in range(1, len(S1)+1):
    for s2 in range(1, len(S2)+1):
        if S1[s1-1] == S2[s2-1]: LCS[s1][s2] = LCS[s1-1][s2-1]+1
        else: LCS[s1][s2] = max(LCS[s1 - 1][s2], LCS[s1][s2 - 1]) 

print(max(map(max,LCS)))