N=int(input())
K=int(input())
sensorList=sorted(list(map(int,input().split())))
disList=[]

if K>=N:
    print(0)
    exit()

for i in range(1,len(sensorList)):
    disList.append(sensorList[i]-sensorList[i-1])

disList=sorted(disList)

for _ in range(K-1):
    disList.remove(max(disList))


print(sum(disList))
