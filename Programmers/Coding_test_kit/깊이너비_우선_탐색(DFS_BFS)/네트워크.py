def solution(n, computers):
    visit=[False for _ in range(n)]
    answer = 0
    
    def dfs(cnt):
        for i in range(n):
            if visit[i]==False and computers[cnt][i]==1:
                visit[i]=True
                dfs(i)
    
    for i in range(n):
        if visit[i]==False:
            answer+=1
            dfs(i)

    return answer