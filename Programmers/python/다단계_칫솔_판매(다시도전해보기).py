def solution(enroll, referral, seller, amount):
    linkedList=dict()
    ansList=dict()
    
    for o,w in zip(enroll,referral):
        linkedList[o]=w
        ansList[o]=0
    
    for s,m in zip(seller,amount):
        price=m*100
        sendPrice=price//10
        price-=sendPrice
        ansList[s]+=price
        
        curName=s
        while linkedList[curName]!='-':
            if sendPrice==0:break
            curName=linkedList[curName]
            receviedPrice=sendPrice
            sendPrice=receviedPrice//10
            ansList[curName]+=receviedPrice-sendPrice
        
    return list(ansList.values())
    
#def solution(enroll, referral, seller, amount):
#    linkedList=dict()
#    amountList=dict()
#    for name in enroll:
#        linkedList[name]=[]
#        amountList[name]=0
#    for i in range(len(referral)):
#        owner,worker=enroll[i],referral[i]
#        if worker!="-":
#            linkedList[owner].append(worker)
#
#    for i in range(len(seller)):
#        amountList[seller[i]]=amount[i]*100
#
#
#    #시나리오에 따라 소득 배분 시작
#    for name in enroll:
#        exit()
#        #재귀를 통해 위에있는 사람을 타고 올라가며 받는 이익을 업데이틑 해주는 방식으로 구현 마무리하기
#
#    answer = []
#    return answer
