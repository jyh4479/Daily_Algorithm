N=int(input())
numList=list(map(int,input().split()))
K=int(input())

numList=sorted(numList)

i,j,ans=0,N-1,0
while(i<j):
    if numList[i]+numList[j]==K:
        ans+=1
        i+=1
        j-=1

    if numList[i]+numList[j]>K:
        j-=1
    elif numList[i]+numList[j]<K:
        i+=1
print(ans)

"""시간효율 안좋음
N=int(input())
numList=list(map(int,input().split()))
K=int(input())

numList=sorted(numList)

ans=0
for i in range(N):
    for j in range(i+1,N):
        if(numList[i]+numList[j]>K):
            break
        if(numList[i]+numList[j]==K):
            ans+=1
print(ans)
"""
