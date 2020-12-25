def solution(n, arr1, arr2): #bin함수 rjust함수를 이용한 파이썬다운 코드
    ans=[]
    for i in range(n):
        a=str(bin(arr1[i]|arr2[i])[2:]).replace("1","#").rjust(n,"0")
        ans.append(a.replace("0"," "))
    return ans

"""먼저 작성한 코드
def change(n,num):
    ans=""
    for i in range(n):
        if 1&num==1:
            ans+="1"
        else:
            ans+="0"
        num>>=1
    return ans[::-1] #거꾸로 출력하는 방법

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
"""