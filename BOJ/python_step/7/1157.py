arr=[0 for _ in range(26)]
s=input()
s=s.upper()
for i in range(len(s)):
    arr[ord(s[i])-65]+=1
max_num=-1
loc=-1
for i in range(len(arr)):
    if(max_num==arr[i]):
        ans="?"
        continue

    max_num=max(max_num,arr[i])
    if(max_num==arr[i]):
        loc=i
        ans=chr(i+65)
print(ans)