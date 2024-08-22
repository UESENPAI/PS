def boj12025():
    PW = list(map(int, list(input().strip())))
    k = int(input().strip())

    numlist = [i for i in range(len(PW)) if PW[i] in [1, 2, 6, 7]]
    num = len(numlist)

    if k > (1<<num):
        print(-1)
        return

    kk = bin(k - 1)[2:].zfill(num)

    for i in range(num):
        idx = numlist[i]
        if kk[i] == '0' and PW[idx] in [6, 7]: PW[idx] -= 5
        elif kk[i] == '1' and PW[idx] in [1, 2]: PW[idx] += 5

    print(''.join(map(str, PW)))

if __name__ == "__main__": boj12025()