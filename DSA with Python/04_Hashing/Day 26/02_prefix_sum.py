arr = [2, 4, 1, 5, 3]

prefix = [0] * len(arr)
prefix[0] = arr[0]
for i in range(1, len(arr)):
    prefix[i] = prefix[i-1] + arr[i]
print(prefix)


'''
Why do we need Prefix Sum?
Suppose you have an array of 1,000 elements and need to calculate the sum between different index ranges many times.

Without prefix sum, you repeatedly traverse the required range.

With prefix sum, you can calculate a range sum using:

Sum(L,R)=prefix[R]-prefix[L-1]


For L=0, simply use prefix[R].

This makes each range-sum query O(1) after O(n) preprocessing.
'''