import sys

N = int(sys.stdin.readline().strip())

ans = 0
kuma = set()
for _ in range(N):
    chat = sys.stdin.readline().strip()
    if chat=="ENTER":
        ans+=len(kuma)
        kuma=set()
    else:
        kuma.add(chat)

ans+=len(kuma)
print(ans)