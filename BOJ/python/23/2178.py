from collections import deque
N,M=map(int,input().split())
graph=[]
for _ in range(N): #맵 정보
    graph.append(list(map(int,input())))

def bfs(i,j):
    q=deque()
    q.append([i,j])
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    while q:
        v=q.popleft()
        for a in range(4):
            nx=v[1]+dx[a]
            ny=v[0]+dy[a]
            if nx<0 or ny<0 or nx>=M or ny>=N:
                continue
            if graph[ny][nx]==1: #처음 방문하는경우
                graph[ny][nx]=graph[v[0]][v[1]]+1 #거리 +1
                q.append([ny,nx])
            else:
                continue

start_i,start_j=0,0
bfs(start_i,start_j)
print(graph[N-1][M-1])