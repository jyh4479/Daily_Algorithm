num=int(input())
step=list(input().split())
x,y=1,1
for i in range(len(step)):
    if(step[i]=="R"):
        if(x+1>num):
            continue
        x+=1
    elif(step[i]=="U"):
        if(y-1<1):
            continue
        y-=1
    elif(step[i]=="D"):
        if(y+1>num):
            continue
        y+=1
    elif(step[i]=="L"):
        if(x-1<1):
            continue
        x-=1
print(y,x)