def solution(prices):
    answer = []
    
    for i in range(len(prices)):
        time=0
        for j in range(i+1,len(prices)):
            time+=1
            if prices[i]>prices[j] or j==len(prices)-1:
                 answer.append(time)
                 break
    answer.append(0)
    return answer

#단순 이중 for로 구현 --> 스택 / 큐로 구현하는 방법 생각해보기
