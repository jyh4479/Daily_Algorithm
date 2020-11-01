num_list=[True for _ in range(246913)] #상한 수 만큼 배열 할당

for i in range(2,123457):
    if(num_list[i]): #해당 수에 대한 방문 확인
        for j in range(i**2,246913,i):
            num_list[j]=False
    else:
        continue

while True:
    num=int(input())
    cnt=0
    if(num==0):
        break
    elif(num==1):
        print(1)
    else:
        down,up=num,num*2
        for i in range(down+1,up+1):
            if(num_list[i]==True):
                cnt+=1
        print(cnt)


