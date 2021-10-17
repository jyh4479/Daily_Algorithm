from collections import deque

def solution(priorities, location):
    q=deque()
    rank=deque()
    for i in range(len(priorities)):
        q.append((priorities[i],i))
        rank.append(priorities[i])

    rank=deque(sorted(rank,reverse=True))
    
    answer=0
    
    while q:
        check=q.popleft()
        if check[0] == rank[0]:
            answer+=1
            
            if check[1]==location:
                break
            
            rank.popleft()
            
        else:
            q.append(check)
    
    return answer
