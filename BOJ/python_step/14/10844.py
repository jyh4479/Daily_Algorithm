N=int(input())

graph=[[0 for _ in range(10)] for _ in range(N+1)] #그래프 생성
for i in range(1,10):
    graph[1][i]=1

if N==1:
    print(sum(graph[N]))
    exit()
else:
    for i in range(2,N+1):
        for j in range(0,10):
            if j==9:
                graph[i][j]=graph[i-1][j-1]
            elif j==0:
                graph[i][j]=graph[i-1][j+1]
            else:
                graph[i][j]=graph[i-1][j-1]+graph[i-1][j+1]
#print(graph)
print(sum(graph[N])%1000000000)
