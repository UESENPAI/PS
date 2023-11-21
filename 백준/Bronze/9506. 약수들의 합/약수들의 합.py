import sys

T=1
while True:
    T = int(sys.stdin.readline().strip())
    divs = set()
    for div in range(1,T//2+1):
        if not T%div:
            divs.add(div)
    divs = sorted(list(divs))
    
    if T == -1:
        break    
    elif T == sum(divs):
        string = ' + '.join(str(div) for div in divs)
        print(f'{T} = {string}')
    else:
        print(f'{T} is NOT perfect.')