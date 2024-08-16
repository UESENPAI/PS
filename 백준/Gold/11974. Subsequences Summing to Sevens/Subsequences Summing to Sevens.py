from sys import stdin, stdout
input = stdin.readline
 
def boj11974():
    N = int(input().strip())
    ints = [int(input().strip()) for _ in range(N)]

    csum, ans = 0, 0
    mods = {}
    mods[0] = -1
    
    for i in range(N):
        csum += ints[i]
        mod = csum % 7
        if mod in mods: ans = max(ans, i - mods[mod])
        else: mods[mod] = i
    print(ans)

if __name__ == '__main__': boj11974()