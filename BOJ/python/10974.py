def printList(ansList):
    for data in ansList:
        print(data, end=" ")
    print()


def dfs(visited, ansList, cnt):
    if cnt == n:
        printList(ansList)
    else:
        for i in range(len(visited)):
            if visited[i] == False:
                visited[i] = True
                ansList.append(i + 1)
                dfs(visited, ansList, cnt + 1)
                ansList.pop()
                visited[i] = False


if __name__ == '__main__':
    global n
    n = int(input())
    ansList = []
    visited = [False for _ in range(n)]

    dfs(visited, ansList, 0)
