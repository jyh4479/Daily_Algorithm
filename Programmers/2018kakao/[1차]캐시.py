from collections import deque

def solution(cacheSize, cities):
    city=[i.upper() for i in cities]
    q=deque()
    cost=0
    if cacheSize==0:
        return len(cities)*5
    for i in city:
        if i in q: #캐시에 존재
            q.remove(i) #최신으로 업데이트
            q.append(i)
            cost+=1
        else: #캐시에 없는경우
            if len(q)>=cacheSize:
                q.popleft()
                q.append(i)
                cost+=5
            else:
                q.append(i)
                cost+=5
    return cost