s = "abcdef"
k = 3
# Print every substring of exactly length k.

# range = 6 - 3 + 1 = 4
 
for i in range(len(s) - k + 1):
    print(s[i:i+k])

