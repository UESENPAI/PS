import sys
input = sys.stdin.readline

def boj1027():
    N = int(input().strip())
    heights = list(map(int,input().strip().split()))
    answer = [0]*N

    for ptr1 in range(N-1) :
      maxSlope = -float('inf')
      for ptr2 in range(ptr1+1, N) :
        slope = (heights[ptr2] - heights[ptr1]) / (ptr2 - ptr1)
        if not slope > maxSlope : continue
        maxSlope = max(maxSlope, slope)
        answer[ptr1] += 1
        answer[ptr2] += 1
        
    print(max(answer))

if __name__ == '__main__': boj1027()
