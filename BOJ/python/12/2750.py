num=int(input())
num_list=[]

def sorting(number_list): #bubble sort
    for i in range(len(number_list)):
        for j in range(i,len(number_list)):
            if(number_list[i]>number_list[j]):
                number_list[i],number_list[j]=number_list[j],number_list[i]

for _ in range(num):
    num_list.append(int(input()))

sorting(num_list)
#num_list.sort() #STL사용

for i in range(num):
    print(num_list[i])