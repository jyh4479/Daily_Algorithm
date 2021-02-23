arr=[-1 for _ in range(26)]
s=input()

for i in range(len(s)):
    if(arr[ord(s[i])-97]==-1):
        arr[ord(s[i])-97]=i
for i in range(len(arr)):
    print(arr[i],end=" ")