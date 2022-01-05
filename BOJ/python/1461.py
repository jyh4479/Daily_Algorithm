import sys

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    numberList = list(map(int, sys.stdin.readline().split()))
    numberList.sort()

    ans = 0
    dataSetList, dataSet = [], []
    plusList, minusList = [], []
    for data in numberList:
        if data < 0:
            minusList.append(data)
        else:
            plusList.append(data)

    for data in minusList:
        dataSet.append(data * (-1))
        if len(dataSet) == m:
            dataSetList.append(dataSet)
            dataSet = []
    if len(dataSet) != 0:
        dataSetList.append(dataSet)
        dataSet = []

    for i in range(len(plusList) - 1, -1, -1):
        data = plusList[i]
        dataSet.append(data)
        if len(dataSet) == m:
            dataSetList.append(dataSet)
            dataSet = []
    if len(dataSet) != 0:
        dataSetList.append(dataSet)
        dataSet = []

    dataSetList = sorted(dataSetList, key=lambda x: x)
    for i in range(len(dataSetList)):
        ans += max(dataSetList[i]) * 2
        if i == len(dataSetList) - 1:
            ans -= max(dataSetList[i])
    print(ans)

# 너무 막 구현함 참고해보자 + 아이디어 도출에 거의 가까웠지만 결국 참고하고 풀이해버림
