from sys import stdin, stdout
input = stdin.readline
 
def boj1394():
    chars = (input().strip())
    pw = (input().strip())
    MOD = 900528
    
    n=len(chars)
    pos = {chars[i]: i + 1 for i in range(n)}

    ans, rdx = 0, 1
    for i in range(len(pw) - 1, -1, -1):
        ans += rdx*pos[pw[i]]
        ans %= MOD
        rdx *= n
        rdx %= MOD

    print(ans % MOD)
 
if __name__ == '__main__': boj1394()