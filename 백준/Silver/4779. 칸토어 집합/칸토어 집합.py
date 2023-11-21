import sys

def Cantorian_set(start, end):
    global s
    ls = (end-start+1)
    if ls < 3:
        return
    div = ls//3

    Cantorian_set(start, start+div-1)

    for i in range(start+div,end-div+1): s[i] = " "

    Cantorian_set(end-div+1, end)

while True:
    try:
        N = sys.stdin.readline().strip()
        if N == '':
            exit()
        else:
            N = int(N)
            s = ['-' for _ in range(3**N)]
            Cantorian_set(0, len(s)-1)
            print(''.join(s))
    except EOFError:
        exit()