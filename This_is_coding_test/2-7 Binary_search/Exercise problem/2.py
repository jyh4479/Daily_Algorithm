#처음 구현한 코드 --> 최대한 덜 잘랐을 경우가 정답인것을 생각해줘야함
N,size=map(int,input().split())
size_list=list(map(int,input().split()))

start,end=0,max(size_list)
ans=-1

while start<=end:
    mid=(start+end)//2
    sum=0
    for i in size_list:
        if i>mid:
            sum+=i-mid
    if sum==size:
        ans=mid
        break
    elif sum>size:
        ans=mid #-->일단 조건을 만족시키는 답을 저장하고 반복문을 돌리면서 더 알맞는 정답을 찾는다
        start=mid+1
    else:
        end=mid-1
print(ans)