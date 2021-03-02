num=int(input())

for _ in range(num):
    a,b,c,d=0,0,0,0
    coin=int(input())

    a=coin//25
    coin%=25

    b=coin//10
    coin%=10

    c=coin//5
    coin%=5

    d=coin//1
    coin%=1

    print("{} {} {} {}".format(a,b,c,d))