num=int(input())

word_list=[]
word_score=dict()
for _ in range(num):
    word_list.append(input())

for word in word_list:
    for i in range(len(word)):
        if word_score.get(word[i]):
            word_score[word[i]]+=10**(len(word)-i-1)
        else:
            word_score[word[i]]=0
            word_score[word[i]]+=10**(len(word)-i-1)

array=sorted(word_score.items(), key=lambda x:x[1], reverse=True)

for i in range(len(array)):
    word_score[array[i][0]]=9-i

ans=0
for word in word_list:
    number=""
    for i in word:
        number+=str(word_score[i])
    ans+=int(number)

print(ans)

