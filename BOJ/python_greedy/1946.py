"""시간초과
import sys
num = int(sys.stdin.readline())

for _ in range(num):
    person_num = int(sys.stdin.readline())
    array_score=[] 
    for _ in range(person_num):
        a,b = map(int,sys.stdin.readline().split())
        array_score.append([a,b])

    #algorithm logic
    ans = len(array_score)
    for i in range(len(array_score)):
        for j in range(len(array_score)):
            if i==j:
                continue
            else:
                if array_score[i][0]>array_score[j][0] and array_score[i][1]>array_score[j][1]: #대소 반대면 최소
                    ans-=1 
                    break
    print(ans)
"""