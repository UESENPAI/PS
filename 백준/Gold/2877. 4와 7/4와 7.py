import sys
input = sys.stdin.readline

def boj2877():
    K = int(input())
    
    digit, count = 0, 0
    while True:
        digit += 1
        prev = count
        count += (2 << (digit-1))
        if not K > count:
            K -= prev
            break
    
    result = ''
    for _ in range(digit):
        result = '4' + result if K % 2 else '7' + result      
        K += 1
        K >>= 1
    
    print(result)

if __name__ == '__main__': boj2877()