import sys
input = sys.stdin.readline

def boj1493():
    length, width, height = map(int, input().strip().split())
    N = int(input().strip())
    AB = [tuple(map(int, input().strip().split())) for _ in range(N)]
    AB.sort(reverse=True)
    
    cnt, buffer = 0, 0
    for Ai, Bi in AB:
        buffer *= 8
        clen = 1<<Ai   
        cubes = (length // clen) * (width // clen) * (height // clen)
        cubes -= buffer
        
        cubes = min(Bi, cubes)
        
        cnt += cubes
        buffer += cubes

    print(cnt) if buffer == length * width * height else print(-1)
        
if __name__ == '__main__': boj1493()