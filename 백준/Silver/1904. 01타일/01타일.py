import sys

N = int(sys.stdin.readline().strip())

switch = True
dp1, dp2 = 1, 2

for n in range(2, N+1):
    if switch:
        dp1 += dp2
        dp1 %= 15746
    else:
        dp2 += dp1
        dp2 %= 15746
    switch = not switch

if switch: print(f'{dp1}')
else: print(f'{dp2}')