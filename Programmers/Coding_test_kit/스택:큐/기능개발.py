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
    check=-1
    count=0
    while numList:
        top=numList.popleft()
        
        if check==-1:
            check=top
            count=1
            continue
            
        if check>=top:
            count+=1
        else:
            ans.append(count)
            numList.appendleft(top)
            count=0
            check=-1
    if count==0:
        return ans
    else:
        ans.append(count)
        return ans
