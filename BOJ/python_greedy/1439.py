num=input()

#1
ans_1=0
if num[0]=="1":
    ans_1=1
before=num[0]

for i in range(1,len(num)):
    if before==num[i]:
        continue
    elif before!=num[i] and num[i]=="1":
        ans_1+=1
    before=num[i]

#0
ans_0=0
if num[0]=="0":
    ans_0=1
before=num[0]

for i in range(1,len(num)):
    if before==num[i]:
        continue
    elif before!=num[i] and num[i]=="0":
        ans_0+=1
    before=num[i]

print(min(ans_0,ans_1))