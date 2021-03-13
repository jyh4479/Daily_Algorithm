import copy #copy하는 함수
from collections import deque

N,M=map(int,input().split())
ansList=[]

#그래프 정보 받기
graph=[]
for _ in range(N):
    graph.append(list(map(int,input().split())))

#BFS실행할 graph DFS로 생성
visitLocation=[]
for i in range(N):
    for j in range(M):
        if graph[i][j]==0: #벽을 세울수있는 공간
            visitLocation.append([i,j])
visit=[False for _ in range(len(visitLocation))] #Location check

def bfs(graph):
    copyGraph=copy.deepcopy(graph) #copy
    
    q=deque()
    for i in range(len(copyGraph)): #바이러스 위치 저장
        for j in range(len(copyGraph[0])):
            if copyGraph[i][j]==2:
                q.append([i,j])
    
    #BFS시작
    dictx=[0,0,1,-1]
    dicty=[1,-1,0,0]
    while(q):
        v=q.popleft()
        
        y,x=v[0],v[1]
        for i in range(4):
            dy=y+dicty[i]
            dx=x+dictx[i]
            if dy<0 or dx<0 or dy>=len(copyGraph) or dx>=len(copyGraph[0]) or copyGraph[dy][dx]==1 or copyGraph[dy][dx]==2: #범위 밖 or 벽인 경우 or 이미 바이러스 있는경우
                continue
            else: #바이러스 전파 가능
                copyGraph[dy][dx]=copyGraph[y][x]
                q.append([dy,dx])
    
    #ans check
    anscheck=0
    for i in range(len(copyGraph)):
        for j in range(len(copyGraph[0])):
            if copyGraph[i][j]==0:
                anscheck+=1
    
    ansList.append(anscheck)


def dfs(index, cnt, graph):
    if cnt==3: #벽을 3개 세우는 모든 경우
        bfs(graph)
    else:
        for i in range(index, len(visit)):
            y=visitLocation[i][0]
            x=visitLocation[i][1]
            if visit[i]==False:
                visit[i]=True
                graph[y][x]=1
                dfs(i,cnt+1,graph)
                graph[y][x]=0
                visit[i]=False

dfs(0,0,graph)

print(max(ansList))


"""
7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0
"""
