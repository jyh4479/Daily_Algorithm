N=int(input())

for _ in range(N):
    num=int(input())
    numList=list(map(int,input().split()))
   
    #logic
    numList=sorted(numList)

    numLeft,numRight=numList[0],numList[0]
    ans=-1
    for i in range(1,len(numList)):
        if i%2 == 1: #홀수
            ans=max(ans,abs(numList[i]-numLeft))
            numLeft=numList[i]
        elif i%2 == 0: #짝수
            ans=max(ans,abs(numList[i]-numRight))
            numRight=numList[i]
    ans=max(ans,abs(numLeft-numRight))
    print(ans)