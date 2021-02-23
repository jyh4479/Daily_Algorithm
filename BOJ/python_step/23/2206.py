import sys
from collections import deque
N,M=map(int,sys.stdin.readline().split())
graph=[list(map(int,sys.stdin.readline().strip())) for _ in range(N)]
move_graph=[[[0 for _ in range(M)]for _ in range(N)]for _ in range(2)]
q=deque()

start_y=0
start_x=0
start_ability=1
dy=[0,0,1,-1]
dx=[1,-1,0,0]


q.append([start_y,start_x,start_ability]) #시작점
ans=0
while q:
    v=q.popleft()
    y,x,ability=v[0],v[1],v[2]

    if y==N-1 and x==M-1:
        ans=move_graph[ability][y][x]+1
        break
   
    for i in range(4):
        ny=y+dy[i] #다음 위치 정의
        nx=x+dx[i]
        nability=ability

        if ny<0 or nx<0 or ny>=N or nx>=M:
            continue

        elif graph[ny][nx]==1 and nability==1: #벽이고 능력이 있는경우
            nability=0
            move_graph[0][ny][nx]=move_graph[1][y][x]+1
            q.append([ny,nx,nability]) #다음 방문 위치 저장

        elif graph[ny][nx]==0 and move_graph[nability][ny][nx]==0:
            move_graph[nability][ny][nx]=move_graph[nability][y][x]+1
            q.append([ny,nx,nability]) #다음 방문 위치 저장

if ans!=0:
    print(ans)
else:
    print(-1)