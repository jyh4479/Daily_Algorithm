import sys
arr=[]
ans=0
ans_arr=[0 for _ in range(42)]
for line in sys.stdin: #입력 받기
    if(line=="\n"):
        break
    ans_arr[int(line)%42]+=1
for i in range(len(ans_arr)):
    if(ans_arr[i]!=0):
        ans+=1
print(ans)