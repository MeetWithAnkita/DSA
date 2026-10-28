# Algorithm	How it works
# Your approach	    Compares the current element with all later elements and swaps immediately
# Bubble Sort	    Compares adjacent elements and swaps them when necessary
# Selection Sort	Finds the minimum element in the remaining unsorted portion, then swaps once

# arr = [5, 2, 8, 1, 3]
# # My approach /////////////////////////
# # def bubble_sort(arr):
# #     for i in range(len(arr)):
# #         for j in range (i+1, len(arr)):
# #             if arr[i] > arr[j]:
# #                 arr[i], arr[j] = arr[j], arr[i]
# #     return arr

# print(bubble_sort(arr))


arr = [5, 2, 8, 1, 3]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print(bubble_sort(arr))

print(bubble_sort([5, 3, 8, 2]))


