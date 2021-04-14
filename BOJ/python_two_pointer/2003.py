#2003 two-pointer
N,M=map(int,input().split())
numList=list(map(int,input().split()))

i,j=0,1
ans=0
while True:
    if j==N+1:
        break
    if sum(numList[i:j+1])==M:
        ans+=1
        i+=1
        j+=1
    elif sum(numList[i:j+1])<M:
        j+=1
    elif sum(numList[i:j+1])>M:
        i+=1
print(ans)