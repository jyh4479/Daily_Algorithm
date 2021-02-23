num=int(input())
man_list=list()

for _ in range(num):
    man_list.append(list(input().split()))

man_list.sort(key=lambda x:(int(x[0]))) #문자열로 받은 숫자를 비교할때는 형변환을 해야한다.

for man in man_list:
    print(man[0],man[1])