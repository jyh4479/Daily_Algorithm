def gcd(a,b):
    if a<b: a,b=b,a
    num,ans=1,0
    while num<=b:
        if b%num==0 and a%num==0: #공약수인경우
            ans=num
        num+=1
    return ans
    

def solution(w,h):
    num=gcd(w,h)
    return (w*h)-(w//num+h//num-1)*num