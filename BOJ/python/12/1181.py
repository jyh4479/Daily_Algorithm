num=int(input())
word_list=list()
word_set=set()
for _ in range(num):
    word_set.add(input())

word_list=list(word_set)
word_list.sort(key=lambda x:(len(x),x))

for word in word_list:
    print(word)
#set자료형에 대한 개념 익히기