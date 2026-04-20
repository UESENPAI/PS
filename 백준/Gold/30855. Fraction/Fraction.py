from sys import stdin
input = stdin.readline

def boj30855():
    from math import gcd

    def norm(a, b):
        if b < 0: a, b = -a, -b
        g = gcd(a, b)
        return a//g, b//g

    def add(x, y):
        return norm(x[0]*y[1] + x[1]*y[0], x[1]*y[1])

    def div(x, y):
        if not y[0]: return None
        return norm(x[0]*y[1], x[1]*y[0])

    n = int(input())
    tokens = input().split()
    if len(tokens) != n:
        print(-1); return

    st = []

    for t in tokens:
        if t == ')':
            try:
                c = st.pop()
                b = st.pop()
                a = st.pop()
                if st.pop() != '(':
                    print(-1); return
            except:
                print(-1); return

            bc = div(b, c)
            if bc is None:
                print(-1); return
            st.append(add(a, bc))

        elif t == '(':
            st.append(t)

        else:
            if not t.isdigit():
                print(-1); return
            st.append((int(t), 1))

    if len(st) != 1 or not isinstance(st[0], tuple):
        print(-1); return

    print(*st[0])

if __name__ == "__main__": boj30855()