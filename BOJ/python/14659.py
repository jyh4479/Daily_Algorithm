if __name__ == "__main__":
    n = int(input())
    numberList = list(map(int, input().split()))

    bestPlayerKill, kill, curPlayerLevel = [0], 0, numberList[0]
    for i in range(1, len(numberList)):
        playerLevel = numberList[i]
        if curPlayerLevel > playerLevel:
            kill += 1
        else:
            bestPlayerKill.append(kill)
            curPlayerLevel = playerLevel
            kill = 0
    print(max(kill, max(bestPlayerKill)))
