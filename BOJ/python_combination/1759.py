from itertools import combinations

sel,N=map(int,input().split())
wordList=list(input().split())
wordList=sorted(wordList)

combi=list(combinations(wordList,sel))

checkList=['a', 'e', 'i', 'o', 'u']

for i in range(len(combi)):
    check="".join(combi[i])
    counta,countb=0,0
    for j in check:
        if j in checkList:
            countb+=1
        else:
            counta+=1
    if counta>=2 and countb>=1:
        print(check)