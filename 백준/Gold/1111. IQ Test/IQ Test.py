import sys
input = sys.stdin.readline

def boj1111():
    N = int(input().strip())
    num = list(map(int, input().strip().split()))
    
    if N<3:
        try:
            print(num[0]) if num[0] == num[1] else print('A')
        except IndexError:
            print('A')
        return
    else:
        if (num[0] - num[1]): a = (num[1] - num[2]) // (num[0] - num[1])
        else: a = 0
        b = num[1] - num[0] * a

        for n in range(N-1):
            if (num[n+1] != num[n] * a + b):
                print('B')
                return
        print(num[-1] * a + b)
    
if __name__ == '__main__': boj1111()
