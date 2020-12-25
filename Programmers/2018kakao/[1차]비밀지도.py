def change(n,num):
    ans=""
    for i in range(n):
        if 1&num==1:
            ans+="1"
        else:
            ans+="0"
        num>>=1
    return ans[::-1]

def solution(n, arr1, arr2):
    A,B=[],[]
    ans=[]
    for i in zip(arr1,arr2):
        A.append(change(n,i[0]))
        B.append(change(n,i[1]))

    for i in zip(A,B):
        text=""
        for j in range(n):
            if i[0][j]=="1" or i[1][j]=="1":
                text+="#"
            else:
                text+=" "
        ans.append(text)
    return ans