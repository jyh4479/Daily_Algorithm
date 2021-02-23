N,M=map(int,input().split())
map=[]
for _ in range(N):
    map.append(str(input()))

mark="WB"
ans=[]
point_y,point_x=0,0
while(point_y+8<=N):
    point_x=0
    start_N=point_y
    end_N=point_y+8
    while(point_x+8<=M):
        start_M=point_x
        end_M=point_x+8

        for i in range(2):
            start_mark=i
            cnt=0
            for a in range(start_N,end_N):
                for b in range(start_M,end_M):
                    if mark[start_mark%2]!=map[a][b]:
                        cnt+=1
                    start_mark+=1
                start_mark+=1
            ans.append(cnt)
        point_x+=1
    point_y+=1

ans.sort()
print(ans[0])