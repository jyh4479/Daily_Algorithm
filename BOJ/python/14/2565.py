import sys
N=int(sys.stdin.readline())
num_list=dict()

for _ in range(N):
    a,b=map(int,sys.stdin.readline().split())
    num_list[a]=b

array=[] #array생성
for i in sorted(num_list):
    array.append(num_list[i])

d=[1]*N
for i in range(N):
    for j in range(i):
        if array[i]>array[j] and d[i]<=d[j]:
            d[i]=d[j]+1
print(N-max(d))