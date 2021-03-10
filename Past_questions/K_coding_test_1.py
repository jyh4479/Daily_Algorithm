#KO---그룹 문제 복기 1
#주어진 문자열로 만들수 있는 조합중 사전순으로 해당 문자열 다음으로 오는 문자 출력
def dfs(str, ansStr,visit, cnt,ansList):
    if(cnt==len(str)):
        ansList.append(ansStr)
    else:
        for i in range(0,len(str)):
            if visit[i]==False:
                visit[i]=True;
                ansStr+=str[i]
                dfs(str,ansStr,visit,cnt+1,ansList)
                ansStr=ansStr[:-1]
                visit[i]=False;

def solution(str):
    ansList=[]
    visit=[False for _ in range(len(str))]
    ansStr=""
    s=sorted(str)
    dfs(s, ansStr, visit, 0,ansList)
    ansList=sorted(ansList)
    print(ansList)

    ans=""
    for i in range(len(ansList)):
        if i==len(ansList)-1:
            ans+=ansList[i]
            break
        if ansList[i]==str:
            ans+=ansList[i+1]
            break

    return ans

print(solution("ABC"))
print(solution("AAA"))
print(solution("DDAB"))