num=int(input())
cnt=1
sum=1
A,B=1,1

while True:
    if A<=num<=B:
        break
    else:
        A=B+1
        sum+=1
        B+=sum
        cnt+=1
dir=cnt
x,y=cnt,1
while(num!=B):
    x+=-1
    y+=1
    B+=-1

if(dir%2==0):
    print("{}/{}".format(x,y))
else:
    print("{}/{}".format(y,x))

"""
시뮬레이션처럼 풀어서 시간초과 나옴
num=int(input())
A=1
B=1
d_A=[1,-1]
d_B=[-1,1]
dir=1 #초기 1 x방향
for _ in range(1,num):
    if(A+d_A[dir]==0):
        B+=1
        dir=0 #방향 전환
        continue
    if(B+d_B[dir]==0):
        A+=1
        dir=1 #방향 전환
        continue

    if(dir==1):
        A+=d_A[dir]
        B+=d_B[dir]
    elif(dir==0):
        A+=d_A[dir]
        B+=d_B[dir]
    
print("{}/{}".format(A,B))
"""