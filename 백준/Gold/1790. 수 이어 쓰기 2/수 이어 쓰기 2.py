import sys
input = sys.stdin.readline

def boj1790():
    N, k = map(int,input().strip().split())

    def getKNum(N, k):

        clen = 0
        digit = 1
        start = 1
        
        while True:
            end = 10**digit - 1
            if end > N: end = N
            count = end - start + 1
            digits = count * digit
            
            if clen + digits >= k:
                index = k - clen - 1
                number = start + index // digit
                numpos = index % digit
                return str(number)[numpos]

            clen += digits
            start = end + 1
            digit += 1
            
            if start > N: break
        
        return -1

    print(getKNum(N, k))

if __name__ == '__main__': boj1790()