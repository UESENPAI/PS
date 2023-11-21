import sys

N = int(sys.stdin.readline().strip())

rdance = {"ChongChong"}

for _ in range(N):
    p = sys.stdin.readline().strip().split()
    if p[0] in rdance or p[1] in rdance:
        rdance.add(p[0])
        rdance.add(p[1])

print(len(rdance))
