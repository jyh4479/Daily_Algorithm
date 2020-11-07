N,M=map(int,input().split())
graph=[]

for i in range(N):
    graph.append(list(map(int,input()))) #그래프 만들기


def dfs(i,j):
    if i<0 or j<0 or i>=N or j>=M:
        return
    if(graph[i][j]==True):
        return
    else:
        graph[i][j]=True
        dfs(i-1,j)
        dfs(i+1,j)
        dfs(i,j+1)
        dfs(i,j-1)

cnt=0
for i in range(N):
    for j in range(M):
        if(graph[i][j]==0): #방문 안한경우
            cnt+=1
            dfs(i,j) #이어지는 구멍 방문처리하기
print(cnt)



"""
15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111


10 10
1111111111
1000100001
1000100001
1000100001
1000100001
1000100001
1000100001
1000100001
1000100001
1000100001
"""