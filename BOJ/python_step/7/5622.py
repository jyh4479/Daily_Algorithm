arr=[0 for _ in range(26)]
for i in range(len(arr)):
    if(chr(i+65)=='A'or chr(i+65)=='B'or chr(i+65)=='C'):
        arr[i]=3
    elif(chr(i+65)=='D'or chr(i+65)=='E'or chr(i+65)=='F'):
        arr[i]=4
    elif(chr(i+65)== chr(i+65)=="G"or chr(i+65)=="H"or chr(i+65)=="I"):
        arr[i]=5
    elif(chr(i+65)=="J"or chr(i+65)=="K"or chr(i+65)=="L"):
        arr[i]=6
    elif(chr(i+65)=="M"or chr(i+65)=="N"or chr(i+65)=="O"):
        arr[i]=7
    elif(chr(i+65)=="P"or chr(i+65)=="Q"or chr(i+65)=="R"or chr(i+65)=="S"):
        arr[i]=8
    elif(chr(i+65)=="T"or chr(i+65)=="U"or chr(i+65)=="V"):
        arr[i]=9
    elif(chr(i+65)=="W"or chr(i+65)=="X"or chr(i+65)=="Y"or chr(i+65)=="Z"):
        arr[i]=10
sum=0
s=input()
for i in range(len(s)):
    sum+=arr[ord(s[i])-65]
print(sum)