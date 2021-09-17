n,m=map(int,input().split())
numberList=list(map(int,input().split()))

ans=0
for i in range(len(numberList)):
    for j in range(len(numberList)):
        if i==j or numberList[i]==numberList[j]:continue
        else: ans+=1

print(ans//2)

#책풀이 다시 체크
