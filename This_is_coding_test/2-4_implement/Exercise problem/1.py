loc=input()
x=int(loc[1])
y=ord(loc[0])-96

dx=[2,2,-2,-2,1,-1,1,-1]
dy=[1,-1,1,-1,2,2,-2,-2]

sum=0
for i in range(8):
    check_x=x+dx[i]
    check_y=y+dy[i]
    if(check_x < 1 or check_y < 1 or check_x > 8 or check_y > 8):
        continue
    else:
        sum+=1
print(sum)