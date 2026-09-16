# Remove special characters
# Example: "Py@th#on!" → "Python"

s = "Py@th#on!"
result = ""
for i in s:
    if i.isalnum():
        result += i
print(result)