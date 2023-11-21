import sys
from collections import deque
 
T = int(sys.stdin.readline().strip())
#assert T<=100
 
for _ in range(T):
    p = sys.stdin.readline().strip()
    #assert len(p)>=1 and len(p)<=100000
    n = int(sys.stdin.readline().strip())
    #assert n>=0 and n<=100000
    if n: x = deque(list(map(int, sys.stdin.readline().strip('[]\n').split(','))))
    else:
        sys.stdin.readline().strip('[]\n')
        x = deque([])
    #for xn in x: assert xn>=1 and xn<=100
 
    flag = 0
    flag2 = True
    for f in p:
        if f == "R":
            flag += 1
        elif f =="D":
            if len(x): x.pop() if flag%2 else x.popleft()
            else:
                flag2 = False
                break

    if flag%2: x.reverse()
    x=list(x)
    print(str(x).replace(' ', '')) if len(x) else print("[]") if flag2 else print("error")