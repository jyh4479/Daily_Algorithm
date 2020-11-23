import sys
N=int(input())
range_list=list()
for _ in range(N):
    range_list.append(list(map(int,sys.stdin.readline().split())))

range_list.sort(key=lambda x:(x[1],x[0]))
#print(range_list)

cnt=0
end_time=0
for time in range_list:
    if end_time<=time[0]: #회의가 끝나고 시작할 수 있는 경우
        end_time=time[1]
        cnt+=1
print(cnt)

"""정렬 조건 체크 못함
N=int(input())
range_list=list()
for _ in range(N):
    range_list.append(list(map(int,input().split())))

range_list.sort(key=lambda x:(x[1])) #-->끝나는 시간이 같은경우 시작 시작도 정렬해줘야함

cnt=0
end_time=0
for time in range_list:
    if end_time==0: #처음 시작하는경우
        end_time=time[1]
        cnt+=1
        continue
    else:
        if end_time>time[0]: #다음 회의 시작 시작이 끝 시간보다 작은경우
            continue
        elif end_time<=time[0]: #회의가 끝나고 시작할 수 있는 경우
            end_time=time[1]
            cnt+=1
            continue
print(cnt)
"""