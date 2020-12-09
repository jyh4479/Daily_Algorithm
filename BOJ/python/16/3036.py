#from collections
#from itertools import combinations #다시 짚어보는 모듈
from fractions import Fraction #분수의 최대 공약수를 구해주는 모듈 --> 속도도 보장됌

N = int(input())
ring_list= list(map(int, input().split()))

for i in range(1, N):
    answer = Fraction(ring_list[0],1)/Fraction(ring_list[i],1)
    print(answer.numerator,'/',answer.denominator,sep = '')

"""처음 풀이는 최대공약수 함수 직접 구현
def gcd(a,b):
    if a<b:
        a,b=b,a
    while b!=0:
        a,b=b,a%b
    return a

N=int(input())
ring_list=list(map(int,input().split()))

a=ring_list[0]
for i in range(1,len(ring_list)):
    if a%ring_list[i]==0:
        print("{}/{}".format(a//ring_list[i],1))
    elif ring_list[i]%a==0:
        print("{}/{}".format(1,ring_list[i]//a))
    elif a%gcd(a,ring_list[i])==0 and ring_list[i]%gcd(a,ring_list[i])==0: #최소 공약수가 존재할때
        c=gcd(a,ring_list[i]) #최소 공약수 구하기
        print("{}/{}".format(a//c,ring_list[i]//c))
    else:
        print("{}/{}".format(ring_list[i],a))
"""