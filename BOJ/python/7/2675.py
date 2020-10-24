cnt=int(input())
for _ in range(cnt):
    num,s=input().split()
    num=int(num)
    new_str=[]
    for i in range(len(s)):
        for j in range(num):
            new_str.append(s[i])
    for i in range(len(new_str)):
        print(new_str[i],end="")
    print("")