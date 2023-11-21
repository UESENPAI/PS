import sys

K = int(sys.stdin.readline())
if K<1 or K>20: raise Exception('Wrong Input!')

arr=[]
harr=[]
varr=[]
for i in range(6):
    D, L = map(int,sys.stdin.readline().split())
    if D not in range(1,5) or L<1 or L>500: raise Exception(f'Wrong Input!')
    if D<3:
        harr.append(L)
        arr.append(L)
    else:
        varr.append(L)
        arr.append(L)

vmaxidx = arr.index(max(varr))
hmaxidx = arr.index(max(harr))

if hmaxidx == 5:
    vs = abs(arr[hmaxidx-1]-arr[hmaxidx-5])
else:
    vs = abs(arr[hmaxidx-1]-arr[hmaxidx+1])

if vmaxidx == 5:
    hs = abs(arr[vmaxidx-1]-arr[vmaxidx-5])
else:
    hs = abs(arr[vmaxidx-1]-arr[vmaxidx+1])

print(f'{K*(arr[vmaxidx]*arr[hmaxidx]-hs*vs)}')