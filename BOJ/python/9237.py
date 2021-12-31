if __name__ == "__main__":
    n = int(input())
    numberList = list(map(int, input().split()))
    numberList.sort(reverse=True)

    completeList = []
    count = len(numberList) - 1
    for data in numberList:
        completeList.append(data - count)
        count -= 1

    print(max(completeList) + len(completeList) + 1)
