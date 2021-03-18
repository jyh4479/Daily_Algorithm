N,M,K=map(int,input().split())
graph=[[0 for _ in range(M)] for _ in range(N)]
size=0

def dfs(y,x):
    dictx=[0,0,1,-1]
    dicty=[1,-1,0,0]
    
    for i in range(4):
        dy=y+dicty[i]
        dx=x+dictx[i]
        if dy<0 or dx<0 or dy>=N or dx>=M or graph[dy][dx]!=0:
            continue
        else:
            graph[dy][dx]=graph[y][x]+1
            dfs(dy,dx)

    global size
    size=max(size,graph[y][x])


for _ in range(K):
    x1,y1,x2,y2=map(int,input().split())
    starty,startx=N-y2,x1
    endy,endx=N-y1-1,x2-1

    for i in range(starty,endy+1):
        for j in range(startx,endx+1):
            graph[i][j]=-1

ans=0
sizeList=[]
for i in range(N):
    for j in range(M):
        if graph[i][j]==0:
            graph[i][j]=1
            ans+=1
            dfs(i,j)
            sizeList.append(size)
        size=0

print(ans)
for i in range(len(sizeList)):
    print(sorted(sizeList)[i],end=" ")
print()
