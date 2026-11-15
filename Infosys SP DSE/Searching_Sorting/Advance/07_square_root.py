'''
Square Root
Given a non-negative integer x, return the integer square 
root of x (the decimal part must be removed).
'''
x = 27
def square_root(x):
    left = 0 
    right = x
    ans = 0 

    while left <= right:
        mid = left + (right - left) // 2 

        if mid * mid <= x:
            ans = mid 
            left = mid + 1 
        else:
            right = mid - 1 

    return ans 

print(square_root(x))
print(square_root(16))  # 4
print(square_root(8))   # 2
print(square_root(0))   # 0

'''
Complexity	Result
Time	    O(log x)
Space	    O(1)
'''
'''
Your code is a general-purpose solution that handles both situations:
1. Non-perfect square: x = 27 → returns 5.
2. Perfect square: x = 36 → returns 6.
'''