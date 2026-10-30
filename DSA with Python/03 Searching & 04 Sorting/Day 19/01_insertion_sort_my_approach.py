arr = [5, 3, 8, 2, 4]

def insertion_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, i):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
        print(arr) 
    return arr

print(insertion_sort(arr))


# Feature	                Your approach	Standard Insertion Sort
# Selects current element	Yes	            Yes
# Checks previous elements	Yes	            Yes
# Moves elements	        Swapping	    Shifting
# Uses key variable	        No	            Yes
# Time complexity	        O(n²)	        O(n²)
# Auxiliary space	        O(1)	        O(1)
