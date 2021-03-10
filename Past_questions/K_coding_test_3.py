#KO---그룹 문제 복기 3
#밖으로 탈출하는데 가장 짧은 길
#조건 1 --> 중앙에서 출발
#조건 2 --> 같은 좌표인 곳은 갈 수 없음 (ex: map[i][i])
#조건 3 --> 중앙좌표 (K,K), 현재 좌표 (X1,Y1), 움직일 좌표 (X2, Y2) MAX(|X1-K|,|Y1-K|)<=MAX(|X2-K|,|Y2-K|)인경우만 이동 가능
#조건 4 --> 같던 곳은 방문 불가
def dfs(x,y,map,visit,N,ans,ansList):
    dictx=[0,0,1,-1]
    dicty=[1,-1,0,0]
    for i in range(4):
        dy=y+dicty[i]
        dx=x+dictx[i]

        if dy==0 or dx==0 or dy==N-1 or dx==N-1: #끝나는 조건
            ans+=map[dy][dx]
            ansList.append(ans)
            ans-=map[dy][dx]
            continue

        checkA=max(abs(x-N//2), abs(y-N//2))
        checkB=max(abs(dx-N//2), abs(dy-N//2))

        if checkB>=checkA: #이동 가능
            if map[dy][dx]!=-1: #같은좌표아닌경우만 이동 가능
                if visit[dy][dx]==False: #방문안한경우 이동가능
                    visit[dy][dx]=True
                    ans+=map[dy][dx]
                    dfs(dx,dy,map,visit,N,ans,ansList)
                    ans-=map[dy][dx]
                    visit[dy][dx]=False


def solution(board,N):
    #--- map 생성 ---#
    ansList=[]
    map=[[0 for _ in range(N)] for _ in range(N)]
    visit=[[False for _ in range(N)] for _ in range(N)]
    for i in range(len(board)):
        map[i//N][i%N]=board[i]
    for i in range(N):
        if i==N//2: continue
        map[i][i]=-1
    #--- map 생성 ---#

    x,y=N//2,N//2
    visit[y][x]=True
    ans=map[y][x]
    dfs(x,y,map,visit,N,ans,ansList)
    
    return min(ansList)

print(solution([9,5,4,9,5,8,5,4,8,5,6,7,8,4,5,1,5,5,9,5,9,8,6,8,7],5))
