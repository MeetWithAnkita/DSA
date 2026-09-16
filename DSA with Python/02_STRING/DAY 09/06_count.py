# Count:
# Alphabets
# Digits
# Spaces
# Special characters
s = "Python 123 @ AI!"
alpha, digit, space, sc = 0, 0, 0, 0
up, low = 0, 0
for i in s :
    if i.isalpha(): 
        alpha += 1 
        if i.isupper():
            up += 1
        else: 
            low += 1
    elif i.isdigit():
        digit += 1
    elif i.isspace():
        space += 1
    else:
        sc += 1
print("Alphabets: ", alpha)
print("Uppercase: ", up)
print("Lowercase: ", low)
print("Digits: ", digit)
print("Spaces: ", space)
print("Special: ", sc)


# ⏱️ Complexity
# Time: O(n)
# Space: O(1)