def solution(citations):
    array = sorted(citations, reverse = True)
    array_check = []

    for i in range(len(array)):
        array_check.append(array[i])
        if len(array_check) > array_check[len(array_check)-1]:
            return i
        elif len(array_check) == array_check[len(array_check)-1]:
            return i+1
    return len(array_check)