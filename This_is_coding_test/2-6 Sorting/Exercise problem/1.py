test_case=int(input())
num_list=[]
for _ in range(test_case):
    num_list.append(int(input()))
for num in sorted(num_list,reverse=True):
    print(num,end=" ")