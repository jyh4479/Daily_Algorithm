stack=[]

stack.append(2)
stack.append(4)
stack.append(5)
stack.append(7)
stack.append(9)
stack.pop()
stack.append(1)
stack.append(2)
stack.pop()

print(stack) #출력 주목
print(stack[::-1])