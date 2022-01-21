if __name__ == "__main__":

    ansList = []
    for _ in range(3):
        numberList = list(map(int, input().split()))
        type = sum(numberList)

        ans = 'D'
        if type == 1:
            ans = 'C'
        elif type == 2:
            ans = 'B'
        elif type == 3:
            ans = 'A'
        elif type == 4:
            ans = 'E'

        ansList.append(ans)

    for ans in ansList:
        print(ans)
