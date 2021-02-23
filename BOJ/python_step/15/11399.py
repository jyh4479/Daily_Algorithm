import sys
N=int(input())
time_list=list(map(int,sys.stdin.readline().split()))
time_list.sort()

num=0
for i in range(N):
    num+=time_list[i]
    time_list[i]=num

print(sum(time_list))