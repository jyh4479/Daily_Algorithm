import sys
num=int(sys.stdin.readline())
stack=[]

for _ in range(num):
    x=int(sys.stdin.readline())
    if x==0:
        stack.pop()
    else:
        stack.append(x)
print(sum(stack))