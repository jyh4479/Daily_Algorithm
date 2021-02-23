import sys
arr=[]
ans_arr=[0 for _ in range(10)]
ans=1
for line in sys.stdin:
    if(line=="\n"):
        break
    arr.append(int(line))

for i in range(len(arr)):
    ans*=arr[i]
ans=str(ans)

for i in range(len(ans)):
    ans_arr[int(ans[i])] += 1

for i in range(len(ans_arr)):
    print(ans_arr[i])