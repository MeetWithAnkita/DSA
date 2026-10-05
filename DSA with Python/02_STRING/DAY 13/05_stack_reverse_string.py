s = "abc"

# result = ""
# for i in range(len(s)-1, -1, -1):
#     result += s[i]
# print(result)

stack = []
for ch in s:
    stack.append(ch)
while stack:
    print(stack.pop(), end="")
