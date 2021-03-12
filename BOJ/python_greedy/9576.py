num=int(input())

for _ in range(num):
    N,M=map(int,input().split())

    bookList=[i+1 for i in range(N)] #책 리스트
    personList=[] #신청 사람 숫자 정보 리스트

    for _ in range(M): #신청 사람 정보 받기
        a,b=map(int,input().split())
        personList.append([a,b])

    #logic
    personList=sorted(personList, key=lambda x:x[1]) #1. 선택의 폭이 좁은 사람 순으로 정렬
    
    ans=0
    for person in personList:
        start=person[0]
        end=person[1]

        for check in range(start,end+1):
            if check in bookList:
                ans+=1
                bookList.remove(check)
                break

    print(ans)
