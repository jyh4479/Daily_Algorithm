def check(a,b):
    b_list=list(b)
    for i in list(a):
        if i in b_list:
            b_list.remove(i)
    if len(b_list)==1:
        return True
    else:
        return False

def solution(begin, target, words):
    ans_list=[]
    if target not in words: #만들 수 없는 경우
        return 0
    visit=[False for _ in range(len(words))] #사용한 단어 체크
    answer=0
    def dfs(cnt,word,answer):
        word_list=list(word)
        for i in list(target):
            if i in word_list:
                word_list.remove(i)
        if len(word_list)==1: #비교 문자가 하나만 다른경우
            answer+=1
            ans_list.append(answer)
            return answer
        else:
            for i in range(len(visit)):
                if visit[i]==False and check(word,words[i]):
                    visit[i]=True
                    answer+=1
                    answer=dfs(cnt+1,words[i],answer)
                    answer-=1
                    visit[i]=False
            return answer
                    
    answer=dfs(0,begin,answer)
    return min(ans_list)