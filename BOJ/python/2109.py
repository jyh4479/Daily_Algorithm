import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    schedule = [0] * 10001
    numberList = []

    for _ in range(n):
        pay, day = map(int, sys.stdin.readline().split())
        numberList.append((pay, day))

    numberList = sorted(numberList, key=lambda x: x[0], reverse=True)

    for data in numberList:
        pay, day = data[0], data[1]

        for i in range(day, 0, -1):

            # 강의 안잡혀있는 경우
            if schedule[i] == 0:
                schedule[i] = pay
                break

    print(sum(schedule))

# 문제에대해 더 다양한 생각을 해야한다.. 왜 이렇게 어렵니
