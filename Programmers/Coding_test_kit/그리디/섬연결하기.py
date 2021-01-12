def solution(n, costs):
    # kruskal algorithm
    ans = 0
    costs.sort(key = lambda x: x[2]) # cost 기준으로 오름차순 정렬
    routes = set([costs[0][0]]) # 집합
    while len(routes)!=n: #사이클에 대한 개념 --> 크루스칼 다시 학습하면서 다지기
        for cost in costs:
            if cost[0] in routes and cost[1] in routes:
                continue
            if cost[0] in routes or cost[1] in routes:
                routes.update([cost[0], cost[1]])
                ans += cost[2]
    return ans

"""
def solution(n, costs):
    costs=sorted(costs,key=lambda x : x[2])
    ans=0
    check=set()

    for i in costs:
        a,b,cost=i[0],i[1],i[2]
        if a in check and b in check: #둘다 집합에 있는경우 넘기기
            continue
        else:
            check.update([a,b])
            ans+=cost
    return ans
"""