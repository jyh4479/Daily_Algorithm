num=int(input())
for _ in range(num):
    letter=input()
    letter=list(letter[::-1].split(" "))
    letter.reverse()
    
    for i in letter:
        print(i,end=" ")
    print()