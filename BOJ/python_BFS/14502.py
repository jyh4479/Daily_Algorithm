from collections import deque

N,M=map(int,input().split())

graph=[[] for _ in range(N+1)]
visit=[False for _ in range(N+1)]
visit[0]=True

def bfs(start,graph):
    q=deque()
    q.append(start)
    visit[start]=True

    while(q):
        v=q.popleft()
        for i in graph[v]:
            if visit[i]==False:
                q.append(i)
                visit[i]=True


#그래프 정보 받기
for i in range(M):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

ans=0
for i in range(len(visit)):
    if visit[i]==False:
        ans+=1
        bfs(i,graph)

print(ans)
