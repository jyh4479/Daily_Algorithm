#조합 구해주는 collections랑 dfs로 다시 풀기
#너무 어렵게 풀었음
def print_num(visit,check_list):
    ans_list=["X" for _ in range(len(check_list[0]))]
    for i in range(len(visit)):
        if visit[i]==True:
            for j in range(len(check_list[i])):
                if ans_list[j]=="X" and check_list[i][j]=="O":
                    ans_list[j]="O"
    if "X" in ans_list:
        return False
    return True

def dfs(idx,cnt,select,visit,check_list,r):
    if cnt==select:
        if(print_num(visit,check_list)):
            return True
        return False
    else:
        for i in range(idx, len(check_list)):
            if visit[i]==False:
                visit[i]=True
                r=dfs(i,cnt+1,select,visit,check_list,r)
                visit[i]=False
                if r==True:
                    return r
        return r

def solution(check_list):
    visit=[False for _ in range(len(check_list))]
    answer=0
    r=False
    for i in range(1,len(check_list)+1):
        if(dfs(0,0,i,visit,check_list,r)):
            answer=i
            break
    return answer

print(solution(["XOXO","OXXO","XXOX","XOOO"]))
print(solution(["OXXO","XOXO","XXOO"]))
print(solution(["OXOXO","OOOOO","XOXOX"]))

"""
#이것도 좀 복잡함 --> 함수로 나눠서 깔끔하게 다시 풀어보기
from itertools import combinations

def solution(check_list):
    visit=[i for i in range(len(check_list))]
    answer=0
    for i in range(1,len(check_list)+1):#선택 개수
        visit_list=list(combinations(visit,i))
        for j in visit_list:
            ans_list=["X" for _ in range(len(check_list[0]))]
            for k in j:
                for a in range(len(check_list[k])):
                    if ans_list[a] == "X" and check_list[k][a] == "O":
                        ans_list[a]="O"
            if "X" not in ans_list:
                answer=i
                break
        if answer!=0:
            break
    return answer
print(solution(["XOXO","OXXO","XXOX","XOOO"]))
print(solution(["OXXO","XOXO","XXOO"]))
print(solution(["OXOXO","OOOOO","XOXOX"]))
"""
