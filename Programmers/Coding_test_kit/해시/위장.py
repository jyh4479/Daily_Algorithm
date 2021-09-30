def solution(clothes):
    answer=1
    itemList=dict()
    
    for item in clothes:
        itemList[item[1]]=list()
        
    for item in clothes:
        itemList[item[1]].append(item[0])
        

    for i in itemList:
        answer*=len(itemList[i])+1
        
    return answer-1
