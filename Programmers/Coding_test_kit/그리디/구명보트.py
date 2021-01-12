def solution(people, limit): #효율성통과못함
    ans=0
    while people:
        item=people.pop() #한명 태우기
        weight=limit-item #태울수있는남은무게
        Max=-1
        for i in people: #나머지중에태울수있는지체크
            if i<=weight and Max<i: 
                Max=i
        if Max==-1:#없는경우
            ans+=1
            continue
        else:#있는경우
            people.remove(Max)
            ans+=1
            continue
    return ans