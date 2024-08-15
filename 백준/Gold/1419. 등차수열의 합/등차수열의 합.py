from sys import stdin, stdout
input = stdin.readline
 
def boj1490():

    l = int(input().strip())
    r = int(input().strip())
    k = int(input().strip())

    if k == 2:
        print(max(r - max(l, 3) + 1, 0))
        
    elif k == 3:
        l = max(l, 6)
        if l > r: print(0)
        else:
            ans = (r // 3) - (l // 3)
            print(ans+1) if not l % 3 else print(ans)
        
    elif k == 4:
        l = max(l, 10)

        if l > r: print(0)

        else:
            ans = (r // 2) - (l // 2)
            if l <= 12 <= r: ans -= 1
            print(ans+1) if not l & 1  else print(ans)
        
    else:
        l = max(l, 15)
        
        if l > r: print(0)
        else:
            ans = (r // 5) - (l // 5)
            print(ans+1) if not l % 5 else print(ans)


if __name__ == '__main__': boj1490()
