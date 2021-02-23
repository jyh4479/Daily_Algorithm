num=int(input())
N=num
k=0
while(num!=1): #k만들기
    num/=3
    k+=1
array=[[False for _ in range(3**k)] for _ in range(3**k)]

def print_star():
    for i in range(N):
        for j in range(N):
            if array[i][j] == False:
                print(" ",end="")
            else:
                print("*",end="")
        print()


def recursive(x,y,N):
    if(N==1):
        array[x][y]=True
        return
    else:
        for i in range(3):
            for j in range(3):
                if(i==1 and j==1):
                    continue
                else:
                    recursive(x+(N//3*i),y+(N//3*j),N//3) ##이 부분 참고

recursive(0,0,N)
print_star()