n,m=map(int,input().split())
numberList=[]

for _ in range(n):
    numberList.append(int(input()))

numberList=sorted(numberList)

start=1
end=numberList[-1]-numberList[0]
result=0

while(start<=end):
    mid=(start+end)//2
    value=numberList[0]
    count=1

    for i in range(1,n):
        if numberList[i]>=value+mid:
            value=numberList[i]
            count+=1
    if count>=m:
        start=mid+1
        result=mid
    else:
        end=mid-1

print(result)

#잘 이해 안됨 다시 풀이하기
