def solution(number, k): #풀이 참고
    stack=[]
    ans=""
    for i,num in enumerate(number):
        while stack and stack[-1]<num and k>0:
            stack.pop()
            k-=1
            if k==0:
                ans+=number[i:]
                break
        stack.append(num)
    if k>0:
        ans="".join(stack[:k+1])
    else:
        ans="".join(stack)
    return ans

"""시간 초과 코드
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
"""