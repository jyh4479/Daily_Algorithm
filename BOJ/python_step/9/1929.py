down,up=map(int,input().split())
num_list=[True for _ in range(up+1)] #상한 수 만큼 배열 할당

for i in range(2,up+1):
    if(num_list[i]): #해당 수에 대한 방문 확인
        for j in range(i+i,up+1,i):
            num_list[j]=False
    else:
        continue

for i in range(down,len(num_list)):
    if(i<2):
        continue
    if(num_list[i]==True):
        print(i)
print("")

""" 기존 소수를 찾는 방법
def search(number):
    if(number==1):
        return False
    else:
        for i in range(2,(number//2)+1):
            if(number%i==0):
                return False
        return True
"""