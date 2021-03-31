N=int(input())

graph=[[0 for _ in range(10)] for _ in range(N+1)] #그래프 생성
for i in range(1,10):
    graph[1][i]=1

if N==1:
    print(sum(graph[N]))
    exit()
else:
    for i in range(2,N+1):
        for j in range(10):
            if j==9:
                graph[i][j]=graph[i-1][j-1]
            elif j==0:
                graph[i][j]=graph[i-1][j+1]
            else:
                graph[i][j]=graph[i-1][j-1]+graph[i-1][j+1]
#print(graph)
print(sum(graph[N])%1000000000)

"""
graph의 i는 계단수의 길이를 뜻하고 j는 해당 숫자가 1의 자리에 오는 경우를 뜻합니다.
즉, j가 끝자리로 올수 있는경우는 i-1에서 j-1, j+1인 경우로 graph[i][j]=graph[i-1][j-1]+graph[i-1][j+1]와 같은 점화식이 성립합니다.
