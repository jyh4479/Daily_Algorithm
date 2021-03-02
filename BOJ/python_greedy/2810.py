num=int(input())
seat=input()
seat_list=[]
seat_list.append("*")
check=0
for i in seat: #자리, 컵 홀더 만들기
    if check==1:
        check=0
        continue
    if i=="S":
        seat_list.append("S")
        seat_list.append("*")
    elif i=="L":
        seat_list.append("L")
        seat_list.append("L")
        seat_list.append("*")
        check=1

#logic
ans=0
for i in range(len(seat_list)):
    if seat_list[i]=="*" or seat_list[i]=="-":
        continue
    else:
        if seat_list[i-1]=="*": #항상 왼쪽부터 탐색
            seat_list[i-1]="-"
            ans+=1
            continue
        if seat_list[i+1]=="*": #왼쪽이 없는 경우 오른쪽 탐색
            seat_list[i+1]="-"
            ans+=1
            continue
print(ans)