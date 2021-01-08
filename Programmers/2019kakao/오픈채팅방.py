def solution(record):
    info=[]
    ans=[]
    id_list=[]
    nick_name=dict()
    for i in record:
        info.append(list(i.split(" ")))

    for i in info:
        if len(i)==3:
            condition,id,name=i[0],i[1],i[2]
        else:
            condition,id=i[0],i[1]

        if condition=="Enter":
            nick_name[id]=name
            id_list.append(id)
            ans.append(id+"님이 들어왔습니다.")
        elif condition=="Leave":
            id_list.append(id)
            ans.append(id+"님이 나갔습니다.")
        elif condition=="Change":
            nick_name[id]=name

    for i in range(len(ans)):
        ans[i]=ans[i].replace(id_list[i],nick_name[id_list[i]])
    return ans