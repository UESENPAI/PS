import sys
input = sys.stdin.readline

def boj12789(N, waiting):
    stack = []
    target = 1
 
    while waiting:
        if waiting[0] == target:
            waiting.pop(0)
            target += 1
        else:
            stack.append(waiting.pop(0))
     
        while stack:
            if stack[-1] == target:
                stack.pop()
                target += 1
            else:
                break
            
    print('Nice' if not stack else 'Sad')
    

if __name__ == "__main__":
    N = int(input().strip())
    waiting = list(map(int,input().strip().split()))
    boj12789(N, waiting)
