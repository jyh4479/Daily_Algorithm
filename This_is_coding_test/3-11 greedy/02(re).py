numbers = list(map(int, input()))
numbers.sort(reverse=True)

result = 0
for num in numbers:
    if result == 0 and num == 0:
        break
    elif result == 0 and num != 0:
        result = num
    elif result != 0 and num == 0:
        break
    else:
        result = result * num

print(result)

#1에 대한 처리가 안됨 --> 0,1은 그냥 더해주기만하면 된다
