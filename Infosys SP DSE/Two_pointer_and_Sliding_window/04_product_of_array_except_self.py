'''
Product of Array Except Self
Medium || LeetCode 238


Given an integer array nums, return an array answer where:
You must solve it without using division, in O(n) time.
'''

# nums = [1, 2, 3, 4]
nums = [2, 3, 0, 4]

def product_array(arr):
    n = len(arr)
    prefix = [1] * n
    for i in range(1, n):
        prefix[i] = prefix[i -1] * arr[i-1] 
    print(prefix)

    sufix = [1] * n
    for i in range(n-2, -1, -1):
       sufix[i] = sufix[i+1] * arr[i+1]
    print (sufix)

    l = []
    for i in range(n):
        l.append(prefix[i] * sufix[i])
    return l

print(product_array(nums))

'''
Complexity	    Your solution
Time	        O(n)
Auxiliary space	O(n)

Your solution satisfies the problem constraints: 
no division and linear time.

Advanced interview improvement: We can optimize auxiliary 
space to O(1), excluding the output array, by storing 
prefix products directly in the answer and maintaining a 
running suffix product.
'''