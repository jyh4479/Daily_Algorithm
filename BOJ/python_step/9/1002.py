import math
test_case=int(input())

for _ in range(test_case):
    x1,y1,r1,x2,y2,r2=map(int,input().split())

    if x1==x2 and y1==y2: #중점이 같은경우
        if(r1==r2): #원이 겹치는 경우
            print(-1)
        else:
            print(0) #원이 겹치지 않는경우
        continue

    else: #중점이 다른경우
        dis_x=abs(x2-x1)
        dis_y=abs(y2-y1)

        dis_dot=dis_x**2+dis_y**2
        add_r=(r1+r2)**2
        sub_r=(r1-r2)**2

        if(dis_dot==add_r or dis_dot==sub_r):
            print(1)
        elif(dis_dot>add_r or dis_dot<sub_r):
            print(0)
        else:
            print(2)