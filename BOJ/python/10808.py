if __name__ == "__main__":
    wordList = [0 for _ in range(26)]
    n = list(input())

    for i in n:
        wordList[ord(i) - 97] += 1

    for i in wordList:
        print(i, end=" ")
    print()
