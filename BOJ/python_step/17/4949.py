import sys
def ans(check):
    stack=[]
    for x in range(len(check)):
        if check[x] == "(":
            stack.append(1)
        elif check[x] == "[":
            stack.append(3)

        else: #닫는 경우
            if len(stack)==0:
                return "no"
            elif check[x]==")" and stack[-1]==1:
                stack.pop()
            elif check[x]=="]" and stack[-1]==3:
                stack.pop()
            else:
                return "no"

    if stack :
        return "no"
    else:
        return "yes"

while(1):
    problem=sys.stdin.readline() #개행을 제거하기위해 strip을 사용해줘야함
    if problem == ".\n":
        break
    elif problem == " .\n":
        print("yes")
    else:
        check=""
        for i in range(len(problem)):
            if problem[i] == "(" or problem[i] == ")" or problem[i] == "[" or problem[i] == "]":
                check+=(problem[i])
        print(ans(check))