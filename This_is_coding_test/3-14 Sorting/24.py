N=int(input())
homes=map(int,input().split())
homes=sorted(homes)

middle=len(homes)//2
if len(homes)%2==0:
    print(homes[middle-1])
else:
    print(homes[middle])
