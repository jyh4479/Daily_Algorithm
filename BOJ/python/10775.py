#유니온 파인드의 대표적인 문제
#저번에는 문제 이해도 안되었는데 이번엔 이해함
#최대 개수가 10^5 라서 이중 루프로 풀면 안됨
#책을 참고해서 유니온 파인드 학습해보기

import sys

sys.setrecursionlimit(10000)


def find_parent(parent, x): #해당함수 최적화됨 비교해보기
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
        return parent[x]
    return x


def union(parent, a, b):
    i = find_parent(parent, a)
    j = find_parent(parent, b)
    parent[i] = j


if __name__ == '__main__':
    g = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    parent = [i for i in range(g + 1)]
    ans = 0

    for _ in range(n):
        data = int(sys.stdin.readline())
        root = find_parent(parent, data)
        if root != 0:
            ans += 1
            union(parent, root, root - 1)
        else:
            break

    print(ans)



#import sys
#sys.setrecursionlimit(10000)
#
#
#def union(parent, a, b):
#    x, y = find_parent(parent, a), find_parent(parent, b)
#    parent[x] = y
#
#
#def find_parent(parent, x):
#    if (parent[x] != x):
#        return find_parent(parent, parent[x])
#    return x
#
#
#if __name__ == '__main__':
#    input = sys.stdin
#    g = int(input.readline())
#    n = int(input.readline())
#    parent = [0] * (g + 1)
#    ans = 0
#
#    for i in range(1, g + 1):
#        parent[i] = i
#
#    for _ in range(n):
#        data = int(input.readline())
#        root = find_parent(parent, data)
#        if root == 0:
#            break
#        union(parent, root, root - 1)
#        ans += 1
#
#    print(ans)
