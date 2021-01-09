def solution(number, k):
    num=len(number)-k #return되는 문자열 길이

    start_point=0
    end_point=len(number)-num+1
    
    ans=""
    for _ in range(num):
        index=start_point
        Max=0
        for i in range(start_point,end_point):
            if int(number[i])>Max:
                index=i
                Max=int(number[i])
        ans+=str(Max)
        start_point=index+1
        end_point+=1
    return ans