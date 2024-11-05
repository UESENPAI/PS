import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def boj2447():
    N=int(input().strip())
    
    def draw_stars(N):
      if N==1: return ['*']

      stars=draw_stars(N//3)
      L=[]

      for star in stars: L.append(star*3)
      for star in stars: L.append(star+' '*(N//3)+star)
      for star in stars: L.append(star*3)

      return L
 
    print('\n'.join(draw_stars(N)))

if __name__ == "__main__": boj2447()