# Find and print:

# All unique characters
# All duplicate characters
# Their frequencies


s = "aabbccddeeffg"
freq = {}
for i in s:
    freq[i] = freq.get(i, 0) + 1
print("Unique Characters: ")
for i in freq:
    if freq[i] == 1 :
        print(i, " -> ",freq[i] )
print("Duplicate Characters: ")
for i in freq:
    if freq[i] > 1 :
        print(i, " -> ",freq[i] )

