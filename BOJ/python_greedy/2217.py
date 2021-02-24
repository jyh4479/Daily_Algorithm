num = int(input())
array = []
for _ in range(num):
    array.append(int(input()))

array = sorted(array, reverse = True)
ans = 0

use_list = []
for i in range(len(array)):
    weight = array[i]
    use_list.append(weight)
    ans = max(ans, weight*len(use_list))

print(ans)