down=int(input())
up=int(input())
num_list=[]

def search(number):
    if(number==1):
        return False
    for i in range(2,(number//2)+1):
        if(number%i==0):
            return False
    return True

sum=0
for i in range(down,up+1):
    if(search(i)):
        num_list.append(i)
        sum+=i
    else:
        continue

if(sum==0):
    print(-1)
else:
    print(sum)
    print(num_list[0])