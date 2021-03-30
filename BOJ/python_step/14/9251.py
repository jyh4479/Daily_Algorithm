A=input()
B=input()

graph=[[0 for _ in range(len(B)+1)] for _ in range(len(A)+1)]

for i in range(len(A)):
    for j in range(len(B)):
        if A[i]==B[j]:
            graph[i+1][j+1]=graph[i][j]+1
        else:
            graph[i+1][j+1]=max(graph[i][j+1],graph[i+1][j])

print(graph[len(A)][len(B)])