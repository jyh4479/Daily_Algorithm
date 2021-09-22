def solution(numberList,start,end):
    if start>end:
        return None

    mid=(start+end)//2

    if mid==numberList[mid]:
        return mid
    elif mid>numberList[mid]:
        return solution(numberList,mid+1,end)
    else:
        return solution(numberList,start,mid-1)

n=int(input())
numberList=list(map(int,input().split()))

ans=solution(numberList,0,n-1)
if ans == None:
    print(-1)
else:
    print(ans)
