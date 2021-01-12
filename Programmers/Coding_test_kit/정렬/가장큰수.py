def solution(num): 
    num = list(map(str, num)) 
    num.sort(key = lambda x : x*3, reverse = True)
    #x*3 --> ex [666,101,222]로 비교
    return str(int(''.join(num)))