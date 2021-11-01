from collections import deque

def solution(n, results):
    players=[i for i in range(1,n+1)]
    canRank=[deque(players) for _ in range(n+1)]
    checkFight=[[] for _ in range(n+1)]
    
    ans=0
    for fight in results:
        win,lose=fight[0],fight[1]
        canRank[win].pop()
        checkRank=canRank[win][0]
        
        while(canRank[lose][0]<=checkRank):
            canRank[lose].popleft()
    
    for i in canRank:
        if len(i)==2:
            ans+=1
    return ans
    
    #그래프로 다시 풀이해보기 --> q로 풀이해보려고 했으나 좋지 않은 방법이다.
