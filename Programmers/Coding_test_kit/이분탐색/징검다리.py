import sys

def solution(distance, rocks, n):
    rocks=sorted(rocks)
    rocks.append(distance)
    start,end=1,distance-1
    answer = 0
    
    while start<=end:
        mid=(start+end)//2
        
        cur=0
        count=0
        ans=sys.maxsize
        
        for rock in rocks:
            if rock<mid+cur:
                count+=1
            else:
                cur=rock
                ans=min(ans,mid)
        
        if count>n:
            end=mid-1
        else:
            start=mid+1
            answer=ans
    
    return answer
