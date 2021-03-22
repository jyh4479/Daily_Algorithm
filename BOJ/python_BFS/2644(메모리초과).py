"""메모리 초과
from collections import deque

#문제에서 제시한 Data 받기
peopleNumber=int(input())
startx,starty=map(int,input().split())

#그래프와 방문 체크를 위한 리스트 생성
N=int(input())
graph=[[]for _ in range(peopleNumber+1)]
visit=[False for _ in range(peopleNumber+1)]

for _ in range(N):
    x,y=map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

#BFS logic
q=deque()
q.append([startx,0]) #시작 부분과 거리 정의
visit[startx]=True
ans=-1
while(q):
    v=q.popleft()
    point,dist=v[0],v[1] #현재 위치와 거리

    if point==starty: #정답을 도출할 정점에 닿았을경우
        ans=dist
        break

    for i in graph[point]: #현재 위치에서 연결되어있는 정점
        if visit[i]==False: #방문하지 않았다면
            q.append([i,dist+1])
    
print(ans)
"""
