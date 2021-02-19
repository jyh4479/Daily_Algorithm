def solution(answers):
    a, a_count = [1,2,3,4,5], 0
    b, b_count = [2,1,2,3,2,4,2,5], 0
    c, c_count = [3,3,1,1,2,2,4,4,5,5], 0

    for i in range(len(answers)):
        if answers[i]==a[i%len(a)]:
            a_count+=1
        if answers[i]==b[i%len(b)]:
            b_count+=1
        if answers[i]==c[i%len(c)]:
            c_count+=1
    
    ans = dict()
    ans[1],ans[2],ans[3]=a_count,b_count,c_count
    ans = (sorted(ans.items(), key = lambda x : x[1], reverse=True))
    
    answer = []
    answer.append(ans[0][0])
    for i in range(1,3):
        if ans[i][1]==ans[i-1][1]:
            answer.append(ans[i][0])
        else:
            return answer
    return answer
