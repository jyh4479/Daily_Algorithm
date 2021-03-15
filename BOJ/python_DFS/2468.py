import copy
import sys
sys.setrecursionlimit(100000);

N=int(input())
graph=[]
ansList=[]
maxValue=-1

def dfs(y,x,copyGraph):
    dictx=[0,0,1,-1]
    dicty=[1,-1,0,0]
    copyGraph[y][x]=-1 #방문을 표시

    for i in range(4):
        dy=y+dicty[i]
        dx=x+dictx[i]
        if dy<0 or dx<0 or dy>=N or dx>=N or copyGraph[dy][dx]==-1:
            continue
        else:
            dfs(dy,dx,copyGraph)

for i in range(N):
    graph.append(list(map(int,input().split())))
    maxValue=max(maxValue, max(graph[i]))

for rain in range(maxValue+1): #각각 비 오는 양을 체크 --> 비가 오지 않은경우 0도 포함시켜야함
    copyGraph=copy.deepcopy(graph) #높이 정보 복사

    for y in range(N):
        for x in range(N):
            if copyGraph[y][x] <= rain:
                copyGraph[y][x] = -1 #물에 잠김을 표시

    ans=0 #copy된 정보로 DFS실행
    for y in range(N):
        for x in range(N):
            if copyGraph[y][x] != -1:
                ans+=1
                dfs(y,x,copyGraph)
    ansList.append(ans)

print(max(ansList))
    

"""
5
6 8 2 6 2
3 2 3 4 6
6 7 3 3 2
7 2 5 3 6
8 9 5 2 7
"""
