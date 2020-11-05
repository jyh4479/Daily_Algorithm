graph=[
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
    ]
visited=[False for _ in range(9)]

stack=[]

start_idx=1
stack.append(start_idx)
visited[start_idx]=True
print(start_idx,end=" ")

while(len(stack)):
    v=stack[-1]

    flag=0
    for i in graph[v]:#방문하지 않은 인접 정점 탐색
        if(visited[i]==False):#방문하지 않은경우
            stack.append(i)
            visited[i]=True
            print(i,end=" ")
            flag=1
            break
        elif(visited[i]==True):
            continue
    if(flag==0):
        stack.pop()
        #주위를 모두 방문했으면 stack삭제
print()