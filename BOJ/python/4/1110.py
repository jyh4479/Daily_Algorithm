ans=0
A=int(input())
compare=A
while True:
    if(A<10):
        A=(A*10)+A
    else:
        A=(((A//10)+(A%10))%10)+(A%10)*10
    ans+=1
    if(A==compare):
        break
print(ans)