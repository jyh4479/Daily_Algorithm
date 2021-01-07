def solution(N, stages): #런타임 에러 발생
    ans=[]
    for stage in range(1,N+1):
        a,b=0,0
        for i in stages:
            if i>=stage: #도전한사람들
                b+=1
            if i==stage: #도전했다가 실패한 사람들
                a+=1
        ans.append(float(a/b))

    index_list=[]
    for i in range(len(ans)):
        index_list.append((i+1,ans[i]))
    
    ans=[]
    while index_list:
        max_value=-1
        max_index=-1
        cur_index=-1
        for i in range(len(index_list)):
            item=index_list[i][1]
            index=index_list[i][0]
            if item>max_value:
                max_value=item
                max_index=index
                cur_index=i
        ans.append(max_index)
        index_list.pop(cur_index)
    return ans