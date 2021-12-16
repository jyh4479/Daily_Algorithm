def solution(lottos, win_nums):
    
    for i in win_nums:
        if i in lottos:
            lottos.remove(i)
    
    best=1
    worst=1
    for i in lottos:
        worst+=1
        best+=1
        if i==0:
            best-=1
        
    if worst>6: worst=6
    if best>6: best=6
    answer = [best,worst]
    return answer
