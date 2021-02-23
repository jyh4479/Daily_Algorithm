N=int(input())
graph=[]
for i in range(N):
    graph.append(list(map(int,input())))

apt_list=[]
apt_num=0
dx=[1,-1,0,0]
dy=[0,0,1,-1]

def dfs(i,j):
    if i<0 or j<0 or i>=N or j>=N:
        return
    if graph[i][j]==0:
        return
    else:
        graph[i][j]=0
        global apt_num
        apt_num+=1
        for a in range(4):
            nx=dx[a]+j
            ny=dy[a]+i
            dfs(ny,nx)


for i in range(N):
    for j in range(N):
        dfs(i,j)
        if apt_num!=0:
            apt_list.append(apt_num)
            apt_num=0

apt_list.sort()
print(len(apt_list))
for i in apt_list:
    print(i)
