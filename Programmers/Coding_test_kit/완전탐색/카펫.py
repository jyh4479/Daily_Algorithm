def solution(brown, yellow):
    block = (brown + 4) // 2
    total_block = brown + yellow

    #block 수를 만들수 있는 경우
    block_list = []
    for i in range(1, block):
        block_list.append([i,block-i])

    for i in block_list:
        a,b = i[0],i[1]
        if a*b == total_block and a>=b:
            return i