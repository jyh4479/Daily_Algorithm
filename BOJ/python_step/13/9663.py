""" 조금 개선하긴 했지만 그래도 시간초과가 난다 (인터넷에서 사용하는 대각선을 따로 1차원 배열로 계산해서 풀어야한다)
import sys
N=int(sys.stdin.readline())
graph=[[0 for _ in range(N)]for _ in range(N)]
ans=0

def check(i,j):
    for x in range(N):
        if graph[x][j]:
            return False
    ny,nx=i-1,j-1
    while(ny>=0 and nx>=0):
        if graph[ny][nx]:
            return False
        ny-=1
        nx-=1

    ny,nx=i-1,j+1
    while(ny>=0 and nx<N):
        if graph[ny][nx]:
            return False
        ny-=1
        nx+=1
    return True


def dfs(cnt):
    if cnt==N:
        global ans
        ans+=1
        return
    else:
        for x in range(N):
            if graph[cnt][x]!=1 and check(cnt,x)==True:
                graph[cnt][x]=1 #체스 놓기
                dfs(cnt+1)
                graph[cnt][x]=0 #체스 회수
dfs(0)
print(ans)
"""

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