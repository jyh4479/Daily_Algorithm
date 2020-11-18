import sys
num=int(sys.stdin.readline())
num_list=[]
count_list={} #최빈값을 위한 dict자료형

def count(num_list):
    for i in num_list:
        count_list[i]=0
    for i in num_list:
        count_list[i]+=1
    ans=sorted(count_list, key=lambda x:(-count_list[x],x)) #sorted를 통해 list로 변경

    if len(ans)==1: #-->num이 1인 경우로 조건을 주면 num은 2, 최빈값 리스트에서 len이 1인경우 오류가 남 (ex 2 -1 -1 입력시)
        return ans[0]
    else:
        if count_list[ans[0]] == count_list[ans[1]]:
            return ans[1]
        return ans[0]

for _ in range(num):
    num_list.append(int(sys.stdin.readline()))

print(round(sum(num_list)/len(num_list)))
print(sorted(num_list)[len(num_list)//2])
print(count(num_list))
print(max(num_list)-min(num_list))
