from collections import deque
num=int(input())
num_list=deque([i for i in range(1,num+1)])
problem_list=list()
for _ in range(num):
    problem_list.append(int(input()))

cal_list=list()
stack=list()
point=0
stack.append(num_list.popleft())
cal_list.append("+")
while stack or num_list: #num_list가 빌때까지
    if len(stack)==0:
        stack.append(num_list.popleft())
        cal_list.append("+")
    elif max(stack)!=problem_list[point]:
        if len(num_list)==0:
            num_list.append(1)
            break
        stack.append(num_list.popleft())
        cal_list.append("+")
    elif max(stack)==problem_list[point]:
        stack.pop()
        cal_list.append("-")
        point+=1

if len(num_list)==0:
    for x in cal_list:
        print(x)
else:
    print("NO")


"""
5
1
2
3
4
5
"""