import sys

def isinsys(x, y, cx, cy, r):
    if (x-cx)**2+(y-cy)**2 < r**2:
        return True
    else:
        return False

def xor(s1, s2):
    return ((s1 and not s2) or (not s1 and s2))

T = int(sys.stdin.readline()) # 테스트 케이스의 개

for _ in range(T):
    x1, y1, x2, y2 = (map(int,sys.stdin.readline().split())) # 출발점 x1, y1 도착점 x2, y2

    n = int(sys.stdin.readline()) # 행성계의 개수 n
    
    cnt = 0
    for i in range(n):
        cx, cy, r = map(int,sys.stdin.readline().split()) # 행정계의 중점과 반지름 Cx Cy r
        if xor(isinsys(x1, y1, cx, cy, r),isinsys(x2, y2, cx, cy, r)): cnt+=1

    print(f'{cnt}')