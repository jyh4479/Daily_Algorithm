if __name__ == "__main__":
    numberList = list(map(int, input().split()))

    prev, up, down = numberList[0], 0, 0
    for data in range(1, len(numberList)):
        if prev < numberList[data]:
            up += 1
        elif prev > numberList[data]:
            down += 1
        prev = numberList[data]

    if up == 0 and down != 0:
        print("descending")
    elif up != 0 and down == 0:
        print("ascending")
    else:
        print("mixed")
