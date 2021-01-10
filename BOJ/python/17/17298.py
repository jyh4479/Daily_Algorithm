N=int(input()) #참고해서 구현
num_list=list(map(int,input().split()))

stack=[]
ans=[-1 for _ in range(N)]
for i in range(len(num_list)):
    while len(stack)>0 and num_list[stack[-1]]<num_list[i]:
        ans[stack.pop()]=num_list[i]
    stack.append(i)

for i in ans:
    print(i,end=" ")
print()

"""시간초과
N=int(input())
num_list=list(map(int,input().split()))

ans=[]
for i in range(N):
    if i==N-1 or num_list[i]>max(num_list[i+1:]):
        print(-1)
    else:
        left=[]
        for j in range(i+1,len(num_list)):
            if num_list[j]>num_list[i]:
                left.append(num_list[j])
                break
        print(left[0])
#스택으로 구현 안함(시간초과) --> 스택으로 구현해보기
"""