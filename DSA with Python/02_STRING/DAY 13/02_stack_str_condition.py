s = "abcde"
# Task: Use a stack to print only the last 3 characters in reverse order.
stack = [] #list

for i in s:
    stack.append(i)

result = ""
for i in range(3):
    result += stack.pop()
print(result)

