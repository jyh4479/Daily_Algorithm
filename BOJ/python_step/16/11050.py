a,b=map(int,input().split())
ans_a=1
ans_b=1
for _ in range(b):
    ans_a*=a
    a-=1
for _ in range(b):
    ans_b*=b
    b-=1
print(ans_a//ans_b)