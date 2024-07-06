import sys
import re

def boj17214():
    input = sys.stdin.readline
    polynomial = input().strip()
    linear, constant = re.findall(r'-?\d*x', polynomial), re.findall(r'[-+]?\d+$', polynomial)

    result = ""
    if polynomial == '0': result = 'W'
    elif polynomial == '1': result = 'x+W'
    else:
        if linear:
            num = linear[0][:-1]
            num = '1' if num == '' or num == '+' else ('-1' if num == '-' else num)
            num = int(num) >> 1
            result += 'xx' if num == 1 else ('-xx' if num == -1 else f'{num}xx')
        if constant:
            num = int(constant[0])
            if num != 0: result += '+x' if num == 1 else ('-x' if num == -1 else (f'+{num}x' if num > 0 and result else f'{num}x'))
        result += '+W'
    
    print(result)

if __name__ == '__main__': boj17214()