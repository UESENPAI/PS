import sys

T = int(sys.stdin.readline().strip())

for _ in range(T):
    cng = int(sys.stdin.readline().strip())
    Q = cng//25
    D = (cng-25*Q)//10
    N = (cng-25*Q-10*D)//5
    P = (cng-25*Q-10*D-5*N)
    print(f'{Q} {D} {N} {P}')
