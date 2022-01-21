if __name__ == "__main__":
    ansList = [0 for i in range(10)]
    numberList = list(map(int, input()))

    for i in numberList:
        if i == 6 or i == 9:
            if ansList[6] > ansList[9]:
                ansList[9] += 1
            else:
                ansList[6] += 1
        else:
            ansList[i] += 1
    print(max(ansList))
