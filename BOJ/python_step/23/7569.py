from collections import deque
import sys
M,N,H=map(int,sys.stdin.readline().split())
graph=[[list(map(int,sys.stdin.readline().split()))for _ in range(N)]for _ in range(H)]
#visit=[[[False for _ in range(M)]for _ in range(N)]for _ in range(H)]

#[H][N][M]
dx=[1,-1,0,0,0,0] #6방향
dy=[0,0,1,-1,0,0]
dh=[0,0,0,0,1,-1]

q=deque()

for i in range(H): #익은 토마토 찾기
    for j in range(N):
        for k in range(M):
            if graph[i][j][k]==1:
                q.append([i,j,k])

ans=0
while q:
    v=q.popleft() #익은 토마토 위치 시작
    for i in range(6):
        nx=v[2]+dx[i]
        ny=v[1]+dy[i]
        nh=v[0]+dh[i]
        if nx<0 or ny<0 or nh<0 or nx>=M or ny>=N or nh>=H:
            continue
        if graph[nh][ny][nx]==0: #덜익은 토마토
            graph[nh][ny][nx]=graph[v[0]][v[1]][v[2]]+1
            q.append([nh,ny,nx])
            ans=max(graph[nh][ny][nx],ans)
        else:
            continue

ans=-1
breaker=0
for i in range(H):
    if breaker==1:
        break
    for j in range(N):
        if 0 in graph[i][j]:
            breaker,ans=1,0
            break
        else:
            ans=max(ans,max(graph[i][j]))
print(ans-1)