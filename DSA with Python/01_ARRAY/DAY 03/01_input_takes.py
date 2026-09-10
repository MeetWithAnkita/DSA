arr = list(map(int, input().split()))
print("Array: ", arr)
print("Number of elements: ", len(arr))

# Time Complexity: O(n)
# Space Complexity: O(n) 
# — because we store n elements in the list.

print("traverse: ")
for i in arr:
    print(i)

# Time: O(n) → every element is visited once.
# Extra Space: O(1) → you only use the variable i.

print("Traversal Using Index: ")
for i in range(len(arr)):
    print("Index: ",i ,"Value: ", arr[i])

# Time: O(n) 
# Extra Space: O(1)