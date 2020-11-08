import sys
sys.setrecursionlimit(10000) #재귀 깊이가 깊어지면 런타임이 발생하므로 선언해준다

def dfs(i,j):
    if i<0 or j<0 or i>=N or j>=M:
        return
    if graph[i][j]==0:
        return
    else:
        graph[i][j]=0
        for a in range(4):
            ny=i+dy[a]
            nx=j+dx[a]
            dfs(ny,nx)

test_case=int(input())
for _ in range(test_case):
    M,N,K=map(int,input().split())

    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    graph=[[0 for _ in range(M)] for _ in range(N)] #밭 정의

    for _ in range(K): #배추 위치 정의
        j,i=map(int,input().split())
        graph[i][j]=1

    cnt=0
    for i in range(N):
        for j in range(M):
            if graph[i][j]==1:
                cnt+=1
                dfs(i,j)
    print(cnt)