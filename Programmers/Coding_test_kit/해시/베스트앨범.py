def solution(genres, plays):
    
    playList=dict()
    
    for i in range(len(genres)):
        genre=genres[i]
        play=plays[i]
        
        if genre not in playList:
            playList[genre]=[0,[]]
        playList[genre][0]+=play
        playList[genre][1].append([i,play])
    
    playList=sorted(playList.items(), key=lambda x:x[1][0], reverse=True)
    
    ans=[]
    for play in playList:
        ansPlay=sorted(play[1][1], key=lambda x:x[1], reverse=True)

        for i in range(len(ansPlay)):
            if i==2:break
            ans.append(ansPlay[i][0])

    return ans
