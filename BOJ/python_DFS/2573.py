from collections import deque

#문제 정보 받기
N,M=map(int,input().split())
graph=[]
visit=[[False for _ in range(M)] for _ in range(N)]
for _ in range(N):
    graph.append(list(map(int,input().split())))

def bfs(y,x):
    distx=[0,0,1,-1]
    disty=[1,-1,0,0]
    q=deque()
    q.append([y,x])
    visit[y][x]=True

    while(q):
        v=q.popleft()
        for i in range(4):
            dy,dx=v[0]+disty[i],v[1]+distx[i]
            if dy<0 or dx<0 or dy>=N or dx>=M:
                continue

            if visit[dy][dx]==False and graph[dy][dx]!=0:
                visit[dy][dx]=True
                q.append([dy,dx])

def melt(y,x):
    distx=[0,0,1,-1]
    disty=[1,-1,0,0]
    num=0
    for i in range(4):
        dy,dx=y+disty[i],x+distx[i]
        if dy<0 or dx<0 or dy>=N or dx>=M:
            continue

        if visit[dy][dx]==False: #주위에 빙하가 있는경우
            num+=1

    return num

#logic
time=0
while True:
    iceNumber=0
    visit=[[False for _ in range(M)] for _ in range(N)]
    for i in range(N): #빙산 개수 세기
        for j in range(M):
            if visit[i][j]==False and graph[i][j]!=0:
                iceNumber+=1
                bfs(i,j)

    if iceNumber==0: #녹일 빙하가 없는경우
        print(0)
        break

    if iceNumber>=2: #문제 조건에 충족하는경우
        print(time)
        break
    
    #빙산 녹이는 logic
    for i in range(N):
        for j in range(M):
            if visit[i][j]==True: #얼음이 있는경우
                graph[i][j]-=melt(i,j)

                if graph[i][j]<0:
                    graph[i][j]=0
    time+=1
