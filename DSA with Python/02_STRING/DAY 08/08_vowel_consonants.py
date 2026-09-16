# Input: Hello World
# Output:
# Vowels: 3
# Consonants: 7

s = "Hello World"
C, V = 0, 0
for i in s:
    if i.isalpha():
        if i not in "aeiouAEIOU":
            C += 1
        else:
            V += 1
print("Vowels: ", V)
print("Consonants: ", C)