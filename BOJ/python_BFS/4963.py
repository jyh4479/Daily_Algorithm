import sys
sys.setrecursionlimit(10000)

def dfs(i,j,graph,N,M):
    dictx=[0,0,1,-1,1,-1,1,-1] #방향 정의
    dicty=[1,-1,0,0,1,-1,-1,1]


    for num in range(8):
        dy=i+dicty[num]
        dx=j+dictx[num]

        if dy<0 or dx<0 or dy>=N or dx>=M or graph[dy][dx]!=1:
            continue
        else:
            graph[dy][dx]=0
            dfs(dy,dx,graph,N,M);
        

while True:
    M,N=map(int,input().split())
    if M==0 and N==0:
        break;
    else:
        #맵 정보 받기
        graph=[]
        for _ in range(N):
            mapList=list(map(int,input().split()))
            graph.append(mapList)
        
        #탐색시작
        ans=0
        for i in range(N):
            for j in range(M):
                if graph[i][j]==1: #갈 수 있는경우
                    ans+=1
                    dfs(i,j,graph,N,M)

        #답 출력
        print(ans)
