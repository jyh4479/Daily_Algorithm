from collections import deque

N=int(input())
graph=[[]for _ in range(N+1)] #연결 정보
dist=[[]for _ in range(N+1)]

for _ in range(N-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

#logic
q=deque()
visit=[False for _ in range(N+1)]
q.append(1) #시작점
visit[1]=True
dist[1].append(0) #root 설정

while(q):
    v=q.popleft()
    for i in graph[v]:
        if visit[i]==False: #방문하지 않은경우
            visit[i]=True
            q.append(i)
            dist[i].append(v) #부모 설정

for i in range(2,N+1):
    print(dist[i][0])
