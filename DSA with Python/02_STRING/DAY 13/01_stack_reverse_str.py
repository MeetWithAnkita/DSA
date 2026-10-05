s = "hello"
stack = []

# 1. Push each character
# 2. Pop each character
# 3. Build reversed string

for i in s:
    stack.append(i)

# for j in range(len(stack)):
#     print(stack.pop(),end="")


result = ""
while stack:
    result += stack.pop()

print(result)
  