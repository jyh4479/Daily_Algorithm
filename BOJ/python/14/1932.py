N=int(input())
num_list=list()
for _ in range(N):
    num_list.append(list(map(int,input().split())))

d=[[0 for _ in range(N)]for _ in range(N)]
d[0][0]=num_list[0][0]
for i in range(1,N):
    for j in range(i+1):
        if j==0:
            d[i][j]=d[i-1][j]+num_list[i][j]
        elif j==N-1:
            d[i][j]=d[i-1][j-1]+num_list[i][j]
        else:
            d[i][j]=max(num_list[i][j]+d[i-1][j-1],num_list[i][j]+d[i-1][j])
print(max(d[N-1]))