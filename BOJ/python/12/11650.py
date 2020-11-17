num=int(input())
num_list=[]
for _ in range(num):
    num_list.append(list(map(int,input().split())))

#num_list.sort(key=lambda x : (x[0],-x[1])) lambda를 사용하여 x[0]의 오름차순 x[1]의 내림차순으로 정렬하는 방법
num_list.sort()

for x in num_list:
    print(x[0], x[1])