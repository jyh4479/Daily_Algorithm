def solution(n, lost, reserve):
    new_lost = set(lost) - set(reserve) #이부분 --> 문제 조건을 놓침
    new_reserve = set(reserve) - set(lost) #이부분 --> 문제 조건을 놓침
    lost_list=list(new_lost)
    for i in lost_list:
        if i-1 in new_reserve:
            new_lost.remove(i)
            new_reserve.remove(i-1)
        elif i+1 in new_reserve:
            new_lost.remove(i)
            new_reserve.remove(i+1)
    return n-len(new_lost)