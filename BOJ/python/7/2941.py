arr=["c=","c-","dz=","d-","lj","nj","s=","z="]
s=input()
sum=0
for i in range(len(arr)):
    s=s.replace(arr[i],"A")
print(len(s))
#참고: https://dpdpwl.tistory.com/119