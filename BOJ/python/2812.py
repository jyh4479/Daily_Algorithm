import sys
from collections import deque

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    numberList = list(map(int, sys.stdin.readline().rstrip('\n')))
    q = deque()

    for data in numberList:
        # 큐에 아무것도 없거나 숫자를 지우지 못하는경우
        if len(q) == 0 or m == 0:
            q.append(data)

        # 비교해서 숫자를 지울지 말지 결정해야하는 경우
        else:
            flag = 1
            while q and m != 0:
                check = q.pop()
                if check < data:
                    m -= 1
                    continue
                else:
                    q.append(check)
                    q.append(data)
                    flag = 0
                    break
            if flag:
                q.append(data)

        # check = q.pop()
        # if data > check:
        #     q.append(data)
        #     m -= 1
        # else:
        #     q.append(check)
        #     q.append(data)

    # 남은 기회 모두 사용하기
    while m > 0:
        q.pop()
        m -= 1

    for data in q:
        print(data, end="")
    print()
