test_case=int(input())

for _ in range(test_case):
    stack=[]
    problem=input()

    for i in range(len(problem)):
        if problem[i] == "(":
            stack.append(1)
        elif problem[i] == ")":
            if len(stack)==0: #비어있는 경우
                stack.append(1)
                break
            else:
                stack.pop()
    if stack : #괄호가 남은경우
        print("NO")
    else:
        print("YES")