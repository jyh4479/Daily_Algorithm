if __name__ == "__main__":
    checkNumber = int(input())
    carNumberList = list(map(int, input().split()))

    ans = 0
    for i in carNumberList:
        if i == checkNumber:
            ans += 1

    print(ans)
