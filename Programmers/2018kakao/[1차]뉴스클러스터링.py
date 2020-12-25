def sum_set(A,B):
    A_list,B_list=list(A),list(B)

    for i in A_list:
        if i in B_list:
            B_list.remove(i)
    #print(A_list+B_list)
    return len(A_list+B_list)

def inter_set(A,B):
    inter_list=[]

    for i in A:
        if i in B:
            inter_list.append(i)
            B.remove(i)
    #print(inter_list)
    return len(inter_list)

def multi_set(string):
    ans_list=[]
    for i in range(len(string)-1):
        sub_string=string[i:i+2]
        if sub_string[0]<'A' or sub_string[0]>'Z' or sub_string[1]<'A' or sub_string[1]>'Z':
            continue
        ans_list.append(sub_string)
    return ans_list

def solution(str1, str2):
    A,B=multi_set(str1.upper()),multi_set(str2.upper())
    C,D=sum_set(A,B),inter_set(A,B)
 
    if C==0:
        ans=1
    else:
        ans=D/C

    return int(ans*65536)

#교집합을 구하는 함수에서 실수있었음