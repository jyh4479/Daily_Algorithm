string=input()
start,end=0,10
for start in range(0,len(string),10):
    print(string[start:end])
    end+=10