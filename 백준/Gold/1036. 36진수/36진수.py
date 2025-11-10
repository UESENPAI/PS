from sys import stdin, stdout
input = stdin.readline
 
def boj1036():
    base=36
    N = int(input().strip())
    nums = [input().strip() for _ in range(N)]
    K = int(input().strip())
    
    value = [0] * base
    for num in nums:
        for i, ch in enumerate(reversed(num)):
            v = int(ch, base)
            value[v] += base ** i

    gain = [(base - 1 - i) * value[i] for i in range(base)]

    change = sorted(range(base - 1), key=lambda i: gain[i], reverse=True)[:K]
    for i in change:
        value[base - 1] += value[i]
        value[i] = 0

    total = sum(i * value[i] for i in range(base))

    if total == 0: print(0)
    res = ''
    while total > 0:
        digit = total % base
        res = (chr(ord('0') + digit) if digit < 10 else chr(ord('A') + digit - 10)) + res
        total //= base
    print(res)

if __name__ == '__main__': boj1036()