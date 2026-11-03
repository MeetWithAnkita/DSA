arr = [5, 2, 5, 3, 2, 5, 4, 3, 2]

'''Tasks:
1. Count the frequency of every element.
2. Store the result in a dictionary.
3. Print the dictionary.
4. Print the frequency of element 5.'''

freq = {}
for i in arr:
    freq[i] = freq.get(i, 0) + 1 
print(freq)
print(freq[5])