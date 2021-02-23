num=int(input())
arr=input().split()
max_num=-1
sum=0

for i in range(len(arr)):#amx값 찾기
    max_num=max(max_num,int(arr[i]))
for i in range(len(arr)):
    sum+=(int(arr[i])/max_num*100)
print(sum/num)