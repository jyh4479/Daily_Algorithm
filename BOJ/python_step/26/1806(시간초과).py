"""sum 함수 때문에 그런가?
import sys
N,K=map(int,input().split())
numList=list(map(int,input().split()))

i,j=0,0
ans=sys.maxsize
while True:
    if j==N:
        break

    if sum(numList[i:j+1])>=K:
        ans=min(ans,j+1-i)
        i+=1
    else:
        j+=1

if ans==sys.maxsize:
    print(0)
else:
    print(ans)
"""
