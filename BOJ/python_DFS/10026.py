import sys
import copy
sys.setrecursionlimit(10000)

N=int(input())
graph=[]
graph2=[]

def dfs(y,x,sel):    
    dictx=[0,0,1,-1]
    dicty=[1,-1,0,0]

    for i in range(4):
        dy=y+dicty[i]
        dx=x+dictx[i]
        if dy<0 or dx<0 or dy>=N or dx>=N or graph[dy][dx]=='x' or graph[dy][dx]!=sel:
            continue
        else:
            graph[dy][dx]='x'
            dfs(dy,dx,sel)
def dfs2(y,x,sel):    
    dictx=[0,0,1,-1]
    dicty=[1,-1,0,0]

    for i in range(4):
        dy=y+dicty[i]
        dx=x+dictx[i]
        if dy<0 or dx<0 or dy>=N or dx>=N or graph2[dy][dx]=='x' or graph2[dy][dx]!=sel:
            continue
        else:
            graph2[dy][dx]='x'
            dfs2(dy,dx,sel)

#그래프 만들기
for _ in range(N):
    graph.append(list(input()))
graph2=copy.deepcopy(graph)
#############

#정상 dfs
ansList=[]
ans=0
for i in range(N):
    for j in range(N):
        if graph[i][j]!='x':
            sel=graph[i][j]
            graph[i][j]='x'
            ans+=1
            dfs(i,j,sel)
ansList.append(ans)

#적록색약 dfs
for i in range(N):
    for j in range(N):
        if graph2[i][j]=='R':
            graph2[i][j]='G'

ans=0
for i in range(N):
    for j in range(N):
        if graph2[i][j]!='x':
            sel=graph2[i][j]
            graph2[i][j]='x'
            ans+=1
            dfs2(i,j,sel)
ansList.append(ans)

print(ansList[0], ansList[1])

