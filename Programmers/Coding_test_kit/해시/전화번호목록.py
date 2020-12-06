def solution(phone_book):
    ans=True
    for i in range(len(phone_book)):
        for j in range(len(phone_book)):
            if i==j:
                continue
            if phone_book[j].find(phone_book[i])==0:
                ans=False
                break
        if ans==False:
            break
    return ans