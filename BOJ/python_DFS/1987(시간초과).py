import sys #시간초과 코드
sys.setrecursionlimit(10000);

N,M=map(int,input().split())
graph=[]
ansList=[]
checkList=[]

def dfs(i,j,ans):
    dictx=[0,0,1,-1]
    dicty=[1,-1,0,0]
    
    for k in range(4):
        dy=dicty[k]+i #다음 좌표
        dx=dictx[k]+j

        if dy<0 or dx<0 or dy>=N or dx>=M:
            continue
        if graph[dy][dx] in checkList: #방문한기록이 있다면
            continue
        else:
            checkList.append(graph[dy][dx])
            ans+=1
            dfs(dy,dx,ans)
            ans-=1
            checkList.remove(graph[dy][dx])
    ansList.append(ans)


for _ in range(N):
    graph.append(list(input()))

ans=1
checkList.append(graph[0][0])
dfs(0,0,ans) #DFS시작
print(max(ansList))

"""
3 4
ABBC
ECED
FGDH
"""