if __name__ == "__main__":
    n = int(input())
    craneList = list(map(int, input().split()))
    m = int(input())
    boxList = list(map(int, input().split()))

    craneList.sort(reverse=True)
    boxList.sort()

    # print(boxList[len(boxList)-1])

    ans = 0
    while boxList:

        # 다 옮길 수 없는 경우
        if boxList[-1] > craneList[0]:
            ans = -1
            break

        for pickup in craneList:

            # 남은 상자가 없는경우
            if len(boxList) == 0:
                break

            # 가장 무거운것 부터 순서대로 크레인이 들수있는지 없는지 체크

            # 가능 하면 들고
            if boxList[-1] <= pickup:
                boxList.pop()

            # 그렇지 않은 크레인은 가능한 가장 무거운 애들부터확인
            else:
                # 옮기기 가능한 가장 무거운것 탐색
                for i in range(len(boxList) - 1, -1, -1):
                    if boxList[i] <= pickup:
                        boxList.pop(i)
                        break

        # 루프가 한번 다 돌면 한번 일한것
        ans += 1
    print(ans)

    # 처음에 들지 못하는 크레인들은 가장 가벼운애들을 픽하면 된다고 접근해서 틀림 (현재 pypy3에서는 돌지만 그냥 python에서는 시간초과)
