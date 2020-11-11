num_list=[5,4,3,2,7,9,1,6,8]

for i in range(len(num_list)):
    min_number=num_list[i]
    min_idx=i
    for j in range(i,len(num_list)):
        if(min_number>num_list[j]):
            min_idx=j
            min_number=num_list[j]
    num_list[i],num_list[min_idx]=num_list[min_idx],num_list[i]

print(num_list)