if __name__ == '__main__':
    N = int(input())
    numberList = sorted(list(map(int, input().split())))

    Sum, ans = 0, 0
    for data in numberList:
        if data > Sum + 1:
            ans = Sum + 1
            break
        else:
            Sum += data

    if ans == 0:
        ans = sum(numberList) + 1

    print(ans)
