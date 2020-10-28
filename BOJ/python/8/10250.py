test_case=int(input())
def number(j,i):
    num=str(j)
    if(i<10):
        num+=("0"+str(i))
    elif(i>=10):
        num+=str(i)
    return num

for _ in range(test_case):
    H,W,N=map(int,input().split())
    room_y=0
    room_x=0
    for i in range(W):
        for j in range(H):
            N-=1
            if(N==0):
                room_y=j+1
                room_x=i+1
                break
        if(N==0):
            break
    print(number(room_y,room_x))