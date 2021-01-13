import functools
def cmp(a,b):
    if str(a)+str(b)>str(b)+str(a):
        return -1
    else:
        return 1
array=[3, 30, 34, 5, 9]
print(sorted(array,key=functools.cmp_to_key(cmp))) #functools 공부해보기

"""
def solution(num): 
    num = list(map(str, num)) 
    num.sort(key = lambda x : x*3, reverse = True)
    #x*3 --> ex [666,101,222]로 비교
    return str(int(''.join(num)))
"""