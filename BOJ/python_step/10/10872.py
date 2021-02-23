num=int(input())

def factorial(num):
    if num==1:
        return 1
    elif num==0:
        return 1
    return num*factorial(num-1)

print(factorial(num))