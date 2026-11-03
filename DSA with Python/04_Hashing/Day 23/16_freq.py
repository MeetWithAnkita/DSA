'''
Your tasks:
1. Create a dictionary to count each element's frequency.
2. Find all elements that appear more than once.
3. Find the total number of distinct elements.
4. Check whether 50 exists in the array using a set.
'''
arr = [10, 20, 10, 30, 20, 40, 10]
freq = {}
for i in arr:
    freq[i] = freq.get(i, 0) + 1 
dupli = set()

for i in freq:
    if freq[i] > 1:
        dupli.add(i)


print(freq)
print("Duplicates: ", dupli)
print("Distinct element: ", len(freq))
arr_set = set(arr)
print("Is 50 present? ", 50 in arr_set)

# Your overall solution takes O(n) average time and O(n) space.