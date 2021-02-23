import sys
N=int(sys.stdin.readline())
num_list=list(map(int,sys.stdin.readline().split()))

d=[1 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if num_list[i]>num_list[j] and d[i]<=d[j]:
            d[i]=d[j]+1
print(max(d))