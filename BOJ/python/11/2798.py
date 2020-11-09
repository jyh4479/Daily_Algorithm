N,M=map(int,input().split())
num_list=list(map(int,input().split()))

max_num=-1
for i in range(0,len(num_list)-2):
    for j in range(i+1,len(num_list)-1):
        for k in range(j+1,len(num_list)):
            sum=num_list[i]+num_list[j]+num_list[k]
            if(sum<=M):
                max_num=max(max_num,sum)
print(max_num)