from collections import deque
N,M=map(int,input().split())
graph=[]
for i in range(N):
    graph.append(list(map(int,input()))) #표현방법 숙지

dx=[1,-1,0,0]
dy=[0,0,1,-1]
start_i,start_j=0,0
q=deque()
q.append([start_i,start_j])

while q:
    v=q.popleft() #현재위치 불러오기

    for i in range(4):
        if v[0]+dy[i]<0 or v[1]+dx[i]<0 or v[0]+dy[i]>=N or v[1]+dx[i]>=M:
            continue
        if(graph[v[0]+dy[i]][v[1]+dx[i]]==0):
            continue

        if(graph[v[0]+dy[i]][v[1]+dx[i]]==1):   
            graph[v[0]+dy[i]][v[1]+dx[i]]=graph[v[0]][v[1]]+1
            q.append([v[0]+dy[i],v[1]+dx[i]]) #다음좌표 저장

print(graph[N-1][M-1])

"""
from collections import deque
N,M=map(int,input().split())
graph=[]
visit=[[False for _ in range(N)]for _ in range(M)] #출발지점 중복 방문 방지
for i in range(N):
    graph.append(list(map(int,input()))) #표현방법 숙지

dx=[1,-1,0,0]
dy=[0,0,1,-1]
start_i,start_j=0,0
q=deque()
q.append([start_i,start_j])
visit[start_i][start_j]=True

while q:
    v=q.popleft() #현재위치 불러오기

    for i in range(4):
        if v[0]+dy[i]<0 or v[1]+dx[i]<0 or v[0]+dy[i]>=N or v[1]+dx[i]>=M:
            continue
        if(graph[v[0]+dy[i]][v[1]+dx[i]]==0):
            continue

        if(graph[v[0]+dy[i]][v[1]+dx[i]]==1 and visit[v[0]+dy[i]][v[1]+dx[i]]==False):   
            visit[v[0]+dy[i]][v[1]+dx[i]]==True
            graph[v[0]+dy[i]][v[1]+dx[i]]=graph[v[0]][v[1]]+1
            q.append([v[0]+dy[i],v[1]+dx[i]]) #다음좌표 저장
print(graph)
"""s
