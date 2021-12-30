from collections import deque

if __name__ == "__main__":
    wordList = list(input())
    leftList, rightList, middleList = [], deque(), []
    wordList.sort()

    wordList = deque(wordList)

    while wordList:
        data = wordList.popleft()

        # 마지막 남은 원소인경우
        if len(wordList) == 0:
            middleList.append(data)
            break

        # 원소 분류
        if data == wordList[0]:
            leftList.append(data)
            rightList.appendleft(wordList.popleft())
        else:
            middleList.append(data)

    if len(middleList) > 1:
        print("I'm Sorry Hansoo")
    else:
        print("".join(leftList), end="")
        print("".join(middleList), end="")
        print("".join(rightList))
