if __name__ == "__main__":
    day = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    month = [(1, 31), (2, 28), (3, 31), (4, 30), (5, 31), (6, 30), (7, 31), (8, 31), (9, 30), (10, 31), (11, 30),
             (12, 31)]

    n, m = map(int, input().split())

    number = 1
    for i in range(len(month)):
        for j in range(1, month[i][1] + 1):
            if i + 1 == n and j == m:
                print(day[number])
                exit()
            number += 1
            number %= 7
