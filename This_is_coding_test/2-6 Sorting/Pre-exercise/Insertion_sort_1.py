num_list=[5,4,3,2,7,9,1,6,8]

for i in range(1,len(num_list)):
    for j in range(i,0,-1):
        if num_list[j]<num_list[j-1]:
            num_list[j],num_list[j-1]=num_list[j-1],num_list[j]
        else:
            break
print(num_list)