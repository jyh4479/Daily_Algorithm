def solution(dartResult):
    ans=[]
    dart_list=list(dartResult)

    for i in range(len(dart_list)):
        if ord("0")<=ord(dart_list[i])<=ord("9"):
            if ord("0")<=ord(dart_list[i+1])<=ord("9"): #10인경우
                ans.append(10)
                continue
            elif ord(dart_list[i])==ord("0") and ord(dart_list[i-1])==ord("1"):
                continue
            else:
                ans.append(int(dart_list[i])) #10미만
                continue

        cur=len(ans)-1
        if dart_list[i]=="D":
            ans[cur]=ans[cur]**2
        elif dart_list[i]=="T":
            ans[cur]=ans[cur]**3
        elif dart_list[i]=="#":
            ans[cur]=ans[cur]*(-1)
        elif dart_list[i]=="*":
            if cur>0:
                ans[cur]*=2
                ans[cur-1]*=2
            else:
                ans[cur]*=2
    return sum(ans)