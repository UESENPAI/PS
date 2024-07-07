import sys
input = sys.stdin.readline

def boj17088():
    N = int(input().strip())
    B = (list(map(int,input().strip().split())))

    if N<3:
        print(0)
        return

    def getd(x1, xn):
        d = (xn-x1)/(N-1)
        return d if d == int(d) else False

    ops = [-1, 0, 1]
    
    cs = []
    for op0 in ops:
        for opn in ops:
            d = getd(B[0] + op0, B[-1] + opn)
            if d: cs.append({ "d": int(d), "op0": op0, "opn": opn })

    cnts = []
    for c in cs:
        a, an, d = B[0] + c["op0"], B[-1] + c["opn"], c["d"]

        cnt = 0
        if c["op0"]: cnt+=1
        if c["opn"]: cnt+=1
        isvalid = True
        for i in range(1, N):
            a += d
            if i == N - 1:
                if an != a:
                    isvalid = False
                    break
            else:
                if B[i] != a and B[i] - 1 != a and B[i] + 1 != a:
                    isvalid = False
                    break
                if B[i] != a: cnt += 1
        if isvalid: cnts.append(cnt)

    print(min(cnts)) if cnts else print(-1)

if __name__ == '__main__': boj17088()