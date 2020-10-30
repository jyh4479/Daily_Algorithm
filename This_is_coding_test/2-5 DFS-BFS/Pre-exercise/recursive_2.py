def factorial_for(num):
    sum=1
    for i in range(num):
        sum*=i+1
    return sum
def factorial_recursive(num):
    if(num==1):
        return 1
    else:
        return num*factorial_recursive(num-1)

print(factorial_for(5))
print(factorial_recursive(5))