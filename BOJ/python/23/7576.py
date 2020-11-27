from collections import deque
M,N=map(int,input().split())
graph=[]
for _ in range(N): #밭 정보 받기
    graph.append(list(map(int,input().split())))

dx=[0,0,1,-1]
dy=[1,-1,0,0]

q=deque()
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1: #토마토 찾기
            q.append([i,j])

while q:
    v=q.popleft()
    for i in range(4):
        nx=v[1]+dx[i]
        ny=v[0]+dy[i]
        if nx<0 or ny<0 or nx>=M or ny>=N:
            continue
        if graph[ny][nx]==0: #안익은 토마토인경우
            graph[ny][nx]=graph[v[0]][v[1]]+1
            q.append([ny,nx])

ans=0
for x in graph:
    if 0 in x:
        ans=0
        break
    else:
        ans=max(ans,max(x))

print(ans-1)