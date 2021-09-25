from collections import deque
import sys

def solution(progresses, speeds):
    n=len(progresses)
    numList=deque()
    for i in range(n):
        count=1
        while count*speeds[i]+progresses[i]<100:
            count+=1
        numList.append(count)
    
    ans=[]
    check=sys.maxsize
    count=1
    while numList:
        value=numList.popleft()
        if check>=value:
            count+=1
        else:
            ans.append(count)
            count=1
            check=sys.maxsize
    
    return ans

#현재 오답
