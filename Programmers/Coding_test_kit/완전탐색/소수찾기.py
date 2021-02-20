from itertools import permutations

def check(num):
    if num is 0 or num is 1:
        return False
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True


def solution(numbers):
    perms = []
    ans = 0
    for i in range(1, len(numbers)+1):
        for c in permutations(numbers, i):
            if int("".join(c)) not in perms:
                perms.append(int("".join(c)))

    for i in perms:
        if check(i) == True:
            ans+=1
    return ans
