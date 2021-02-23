num=int(input())
breaker=0
for i in range(num):
    num_list=str(i)
    new_num=i
    for j in range(len(num_list)):
        new_num+=int(num_list[j])
    if new_num==num:
        print(i)
        breaker=1
        break
if breaker==0:
    print(0)