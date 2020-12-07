def solution(price):
    answer=[]
    for i in range(len(price)):
        ans=-1
        day=0
        cur_price=price[i]
        for j in range(i+1,len(price)):
            day+=1
            if cur_price<price[j]:
                ans=day
                answer.append(ans)
                break
            if j==len(price)-1:
                answer.append(ans)
    answer.append(-1)
    return answer

print(solution([13,7,3,7,5,16,12]))