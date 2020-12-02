def solution(numbers, target):
    answer=0

    def dfs(cnt,ans,answer):
        if cnt==len(numbers):
            if ans==target: return answer+1
            else: return answer

        else:
            for i in range(2):
                if i==0:
                    answer=dfs(cnt+1,ans+numbers[cnt],answer)
                elif i==1:
                    answer=dfs(cnt+1,ans-numbers[cnt],answer)
            return answer

    answer=dfs(0,0,answer)
    return answer
print(solution([1,1,1,1,1],3))

"""
def solution(numbers, target):
    visit=[False for _ in range(len(numbers))]

    def dfs(cnt,ans,answer):
        if cnt==len(numbers) and ans==target:
            return answer+1
        else:
            for j in range(2):
                for i in range(cnt,len(numbers)):
                    if j == 0:
                        num=numbers[i]
                    else:
                        num=-numbers[i]

                    if visit[i]==False:
                        visit[i]=True
                        ans+=num
                        answer=dfs(cnt+1,ans,answer)
                        ans-=num
                        visit[i]=False
            return answer

    answer=dfs(0,0,0)
    return answer
"""