import sys

N, M = map(int,sys.stdin.readline().split())

pokedex_no = {}
pokedex_name = {}

for n in range(N):
    name = sys.stdin.readline().strip()
    pokedex_no[n] = name
    pokedex_name[name] = n
    

for _ in range(M):
    q = sys.stdin.readline().rstrip()
    if q.isnumeric():
        print(f'{pokedex_no[int(q)-1]}')
    else:
        print(f'{pokedex_name[q]+1}')
