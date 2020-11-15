"""시간 초과 나는 코드
N=int(input())
map=[[0 for _ in range(N)] for _ in range(N)]

dy=[1,1,1,0,0,-1,-1,-1]
dx=[1,0,-1,1,-1,1,0,-1]
ans=0
def dfs(a,cnt):
    if cnt==0: #모두 다 놓은 경우
        global ans
        ans+=1
        return

    for i in range(a,N):
        for j in range(N):
            if map[i][j] == 0: #공격 받지 않는 장소라면

                map[i][j]+=1 #놓는 자리 설정
                for a in range(8): #놓은 자리에서 모든 방향으로 공격하는 루트 설정
                    ny=i
                    nx=j
                    while True:
                        ny+=dy[a]
                        nx+=dx[a]
                        if ny<0 or nx<0 or ny>=N or nx>=N: #범위에 벗어나는 경우
                            break
                        else: #범위내에 있는 경우 체크
                            map[ny][nx]+=1
                dfs(i+1,cnt-1)

                map[i][j]-=1
                for a in range(8): #놓은 자리에서 모든 방향으로 공격하는 루트 설정
                    ny=i
                    nx=j
                    while True:
                        ny+=dy[a]
                        nx+=dx[a]
                        if ny<0 or nx<0 or ny>=N or nx>=N: #범위에 벗어나는 경우
                            break
                        else: #범위내에 있는 경우 체크
                            map[ny][nx]-=1
            else: #공격 받는 장소
                continue


dfs(0,N)
print(ans)
"""