a1,b1=map(int,input().split())
a2,b2=map(int,input().split())
a3,b3=map(int,input().split())

if(a1==a2):
    ans_a=a3
elif(a2==a3):
    ans_a=a1
elif(a1==a3):
    ans_a=a2

if(b1==b2):
    ans_b=b3
elif(b2==b3):
    ans_b=b1
elif(b1==b3):
    ans_b=b2

print(ans_a,ans_b)
