import sys
input = sys.stdin.readline

def boj19940():
    T = int(input().strip())
    TCs = [int(input().strip()) for _ in range(T)]

    for TC in TCs:
        buffer = TC
        
        ADDH = buffer // 60
        buffer %= 60
        
        ADDT = buffer // 10
        buffer %= 10
        
        ADDO = buffer

        if ADDO>5:
            ADDT+=1
            ADDO-=10
            
        if ADDT>3:
            ADDH+=1
            ADDT-=6
            
        if ADDT<0 and ADDO==5:
            ADDT+=1
            ADDO-=10
            
        MINT = abs(ADDT) if ADDT < 0 else 0
        MINO = abs(ADDO) if ADDO < 0 else 0

        if ADDT < 0: ADDT = 0
        if ADDO < 0: ADDO = 0
        
        ans = (ADDH, ADDT, MINT, ADDO, MINO)
        print(*ans)

if __name__ == '__main__': boj19940()