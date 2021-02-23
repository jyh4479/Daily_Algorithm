import sys
test_case=int(sys.stdin.readline())

stack=[]
for _ in range(test_case):
    com_list=list(sys.stdin.readline().split())
    if com_list[0]=="push":
        stack.append(int(com_list[1]))
    elif com_list[0]=="top":
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])
    elif com_list[0]=="size":
        print(len(stack))
    elif com_list[0]=="empty":
        if len(stack)==0:
            print(1)
        else:
            print(0)
    elif com_list[0]=="pop":
        if len(stack)>0:
            print(stack.pop())
        else:
            print(-1)
#https://chunghyup.tistory.com/37 직접 구현하는 방법