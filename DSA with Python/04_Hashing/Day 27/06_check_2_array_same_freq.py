'''
Question: Check whether two arrays have the same frequency of elements.

'''

arr1 = [1, 2, 2, 3, 3, 3]
arr2 = [3, 2, 1, 3, 2, 3]

def check_same_freq(arr1, arr2):
    if len(arr1) != len(arr2):
        return False
    freq = {}
    for i in arr1:
        freq[i] = freq.get(i, 0) + 1 
    for i in arr2:
        if i in freq:
            freq[i] -= 1 
            if freq[i] == 0:
                del freq[i]
        else:
            return False
    if freq:
        return False 
    else:
        return True

print(check_same_freq(arr1, arr2))