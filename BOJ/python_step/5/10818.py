cnt=int(input())
arr=list(map(int,input().split()))
max_num=-1000001
min_num=1000001

for i in range(0,cnt):
    max_num=max(max_num,arr[i])
    min_num=min(min_num,arr[i])

print(str(min_num)+" "+str(max_num))
#print("{} {}".format(min_num,max_num))