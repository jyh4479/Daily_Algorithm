sum=0
def del_duplicate(s):
    result=s[0]
    for i in range(1,len(s)):
        if(result[len(result)-1]!=s[i]):
            result+=s[i]
    return result

cnt=int(input())
for i in range(cnt):
    check=[0 for _ in range(26)]
    sum+=1
    s=input()
    s=del_duplicate(s)
    for i in range(len(s)):
        check[ord(s[i])-97]+=1
        if(check[ord(s[i])-97]>1):
            sum-=1
            break
print(sum)