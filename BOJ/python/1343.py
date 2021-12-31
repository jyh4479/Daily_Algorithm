if __name__ == "__main__":
    dataList = list(input())

    count, ans = 0, ""
    for i in range(len(dataList)):
        if dataList[i] == "X":
            count += 1
        elif dataList[i] == ".":
            ans += "."
            if count % 2 == 1:
                ans = -1
                break

        if count == 4:
            ans += "AAAA"
            count = 0
        elif count == 2 and (i + 1 >= len(dataList) or dataList[i + 1] == "."):
            ans += "BB"
            count = 0

    if count % 2 == 1:
        ans = -1
    print(ans)

#너무 대충풀었음
