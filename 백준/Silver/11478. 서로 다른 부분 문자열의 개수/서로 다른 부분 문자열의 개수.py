import sys

S = sys.stdin.readline().strip()

substr = set()
for i in range(len(S)):
    for j in range(i, len(S)):
        substr.add(S[i:j+1])
print(len(substr))