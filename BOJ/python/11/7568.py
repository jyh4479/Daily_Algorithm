num=int(input())
person_list=[]
for _ in range(num):
    person_list.append(list(map(int,input().split())))

for i in range(num):
    k=1
    for j in range(num):
        if i==j: #같은 사람을 비교하는 경우
            continue
        else:
            if person_list[i][0] < person_list[j][0] and person_list[i][1] < person_list[j][1]:
                k+=1
            #elif person_list[i][0] == person_list[j][0] and person_list[i][1] < person_list[j][1]:
             #   k+=1
            #elif person_list[i][0] < person_list[j][0] and person_list[i][1] == person_list[j][1]:
             #   k+=1
    print(k,end=" ")
print()