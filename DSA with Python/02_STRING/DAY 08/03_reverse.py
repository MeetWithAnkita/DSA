a = input()

reverse = "" #blank string
for i in a:
    reverse = i + reverse
print(reverse)

print(a[::-1])