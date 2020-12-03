def solution(tickets):
    visit=[False for _ in range(len(tickets))]#티켓 사용여부 체크
    ans=["ICN"]
    ans_list=[]
    
    def dfs(cnt,start,ans):
        if cnt==len(visit):#모든 티겟 사용시
            copy=list(ans) # ex 그냥 ans를 append해버리면 값이 아닌 주소를 전달한것이므로 값이 계속 변한다
            ans_list.append(copy)
            return
        else:
            for i in range(len(visit)):
                if visit[i]==False and tickets[i][0]==start:#티켓을 사용하지 않았고 출발지가 동일한경우
                    visit[i]=True #티켓사용
                    ans.append(tickets[i][1])
                    dfs(cnt+1,tickets[i][1],ans)#도착지를 시작지로 설정
                    ans.pop()
                    visit[i]=False
  
    dfs(0,ans[0],ans)
    return min(ans_list)