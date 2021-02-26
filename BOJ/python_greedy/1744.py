num=int(input())

numPlusList=[]
numMinusList=[]
numZeroList=[]
for _ in range(num):
    number=int(input())
    if number<0:
        numMinusList.append(number)
    elif number>0:
        numPlusList.append(number)
    else:
        numZeroList.append(number)

#음수와 0에 대한 처리가 관건
#Algorithm logics --> 반례하나를 생각못함 1은 곱하는게 아니라 더해야 더 큰값이 된다
numPlusList=sorted(numPlusList, reverse=True)
numMinusList=sorted(numMinusList)

ans_list=[]
for i in range(0,len(numPlusList),2):
    if i+1>=len(numPlusList):
        ans_list.append(numPlusList[i])
    else:
        if numPlusList[i]==1 or numPlusList[i+1]==1:
            ans_list.append(numPlusList[i])
            ans_list.append(numPlusList[i+1])
        else:
            ans_list.append(numPlusList[i]*numPlusList[i+1])

for i in range(0,len(numMinusList),2):
    if i+1>=len(numMinusList):
        if len(numZeroList)>0:
            numZeroList.remove(0)
        else:
            ans_list.append(numMinusList[i])
    else:
        ans_list.append(numMinusList[i]*numMinusList[i+1])

print(sum(ans_list))