import sys
from collections import deque
N,M=map(int,sys.stdin.readline().split())
graph=[list(map(int,sys.stdin.readline().strip())) for _ in range(N)]
move_graph=[[0 for _ in range(M)]for _ in range(N)]
q=deque()

start_y=0
start_x=0
start_ability=1
dy=[0,0,1,-1]
dx=[1,-1,0,0]

q.append([start_y,start_x,start_ability]) #시작점
while q:
    v=q.popleft()
    y,x,ability=v[0],v[1],v[2]
    for i in range(4):
        ny=y+dy[i] #다음 위치 정의
        nx=x+dx[i]
        if ny<0 or nx<0 or ny>=N or nx>=M:
            continue
        if graph[ny][nx]!=1: #벽이 아닌경우
            move_graph[ny][nx]=move_graph[y][x]+1
            q.append([ny,nx,ability]) #다음 방문 위치 저장
            if ny==N-1 and nx==M-1:
                q.clear()
                break
        elif graph[ny][nx]==1 and ability==1:
            ability=0
            move_graph[ny][nx]=move_graph[y][x]+1
            q.append([ny,nx,ability]) #다음 방문 위치 저장
            if ny==N-1 and nx==M-1:
                q.clear()
                break

if move_graph[ny][nx]==0:
    print(-1)
else:
    print(move_graph[ny][nx]+1)