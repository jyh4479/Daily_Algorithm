import collections
def solution(participant, completion):
    ans=collections.Counter(participant)-collections.Counter(completion) #Counter로 원소들의 개수를 셀수있음
    return  list(ans)[0]