if __name__ == '__main__':
    # 초 단위
    time = int(input())

    # 5분 1분 10초
    timeList = [300, 60, 10]
    ansList = [0, 0, 0]

    if time % 10 != 0:
        print(-1)
    else:
        while time > 0:
            for i in range(len(timeList)):
                curTime = timeList[i]
                while time >= curTime:
                    time -= curTime
                    ansList[i] += 1

        for ans in ansList:
            print(ans, end=" ")
        print()
