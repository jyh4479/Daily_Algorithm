""" 시간 초과
from collections import deque

N=int(input())
graph=[]
for _ in range(N):
    graph.append(list(map(int,input().split())))

def search(graph):
    for i in range(N):
        for j in range(N):
            if graph[i][j]==9:
                return i,j

def checkEat(size):
    for i in range(N):
        for j in range(N):
            if graph[i][j]!=0 and graph[i][j]<size:
                return True #먹을 수 있는 물고기가 있는경우
    return False #먹을 수 있는 물고기가 없는경우

starty,startx=search(graph)
size=2
eat=0
ans=0
while(checkEat(size)):
    distGraph=[[0 for _ in range(N)] for _ in range(N)]
    visit=[[False for _ in range(N)] for _ in range(N)]
    disty=[-1,0,0,1]
    distx=[0,-1,1,0]
    q=deque()
    q.append([starty,startx])
    visit[starty][startx]=True
    graph[starty][startx]=0

    while q:
        v=q.popleft()
        for i in range(4):
            dy=v[0]+disty[i]
            dx=v[1]+distx[i]
            if dy<0 or dx<0 or dy>=N or dx>=N or visit[dy][dx]==True or graph[dy][dx]>size:
                continue
            else:
                distGraph[dy][dx]=distGraph[v[0]][v[1]]+1
                visit[dy][dx]=True
                q.append([dy,dx])
   
    checkDis=9999
    checki,checkj=0,0
    for i in range(N):
        for j in range(N):
            if graph[i][j]!=0 and graph[i][j]<size and distGraph[i][j]<checkDis:
                checki,checkj=i,j
                checkDis=distGraph[i][j]

    ans+=distGraph[checki][checkj]
    eat+=1
    if eat==size:
        size+=1
        eat=0
    graph[checki][checkj]=9
    starty,startx=checki,checkj

print(ans)
"""
