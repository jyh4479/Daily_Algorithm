import sys

N=int(sys.stdin.readline().rstrip())
array=[]
d=[0]*10001
for _ in range(N):
    array.append(int(sys.stdin.readline().rstrip()))

if N==1:
    print(array[0])
elif N==2:
    print(max(array[0],array[0]+array[1]))
else:
    d[0]=array[0]
    d[1]=max(array[0],array[0]+array[1])
    d[2]=max(array[0]+array[1],array[1]+array[2],array[0]+array[2])
    for i in range(3,N):
        d[i]=max(d[i-3]+array[i-1]+array[i],d[i-3]+array[i-2]+array[i],d[i-1])
        #d[i-3]+array[i-2]+array[i] --> d[i-2]+array[i] (무슨차이?)
        #예상으로는 d[i-3]부분이 겹치면서 발생하는 문제 같음
    print(d[N-1])