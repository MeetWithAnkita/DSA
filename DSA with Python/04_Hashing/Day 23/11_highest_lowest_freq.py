arr = [1, 2, 2, 3, 3, 3, 4, 2, 3]

freq = {}
for i in arr:
    freq[i] = freq.get(i, 0) + 1 

h_ele = []
l_ele = []
h = float('-inf')
l = float('inf')

for i in freq:
    if freq[i] > h:
        h = freq[i]
        h_ele.clear()
        h_ele.append(i)
    elif freq[i] == h:
        h_ele.append(i)

    if freq[i] < l:
        l = freq[i]
        l_ele.clear()
        l_ele.append(i)
    elif freq[i] == l:
        l_ele.append(i)

print(freq)
print("Highest freq element: ", h_ele)
print("Lowest freq element: ", l_ele)

'''
Complexity	            Value
Frequency counting	    O(n) average
Finding highest/lowest	O(k)
Total time	            O(n + k) = O(n)
Space	                O(k)
'''



