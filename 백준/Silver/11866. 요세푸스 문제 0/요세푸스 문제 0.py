import sys
from collections import deque

N, K = map(int, sys.stdin.readline().strip().split())

en = deque([_ for _ in range(1,N+1)])
Josephus = []

while len(en):
    for _ in range(K-1): en.append(en.popleft())
    Josephus.append(en.popleft())
    
print(f"<{', '.join(map(str, Josephus))}>")
