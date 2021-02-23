problem=input()
number_list=list()
sum_list=list()
number=""

for i in range(len(problem)):
    if(problem[i]=="-"):
        sum_list.append(int(number))
        number=""
        number_list.append(sum(sum_list))
        sum_list.clear()
        continue
    elif(problem[i]=="+"):
        sum_list.append(int(number))
        number=""
        continue
    elif(i==len(problem)-1):
        number+=problem[i]
        sum_list.append(int(number))
        number_list.append(sum(sum_list))
        break
    number+=problem[i]

ans=number_list[0]
for i in range(1,len(number_list)):
    ans-=number_list[i]
print(ans)
