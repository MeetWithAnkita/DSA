s = "Python123is45Fun6"
result = ""
for i in s:
    if not i.isdigit():
        result += i
print(result)


# Complexity
# Time: O(n²) in Python because repeated string concatenation creates new strings.
# Space: O(n)