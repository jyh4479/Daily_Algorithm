test_case=int(input())

def check_num(a):
    if a == 1 : 
        return False
    else:
        for i in range(2,a):
            if(a%i==0):
                return False
        return True

for _ in range(test_case):
    num=int(input())
    for i in range(num//2,1,-1):
        a=i
        b=num-a
        if(check_num(a) and check_num(b)):
            print(a,b)
            break

################################################
"""시간 초과
test_case=int(input())
num_check=[True for _ in range(10001)]
num_list=[]

for i in range(2,10001):
    for j in range(i**2,10001,i):
        num_check[j]=False

for i in range(2,10001): #소수 list만들기
    if(num_check[i]==True):
        num_list.append(i)


for _ in range(test_case):
    num=int(input())
    for i in range(len(num_list)):
        a=num_list[i]
        for j in range(i,len(num_list)):
            b=num_list[j]
            if(a+b==num):
                ans_a=a
                ans_b=b
    print(ans_a,ans_b)
"""