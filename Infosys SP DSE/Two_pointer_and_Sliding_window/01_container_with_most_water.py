'''
Difficulty: Medium, LeetCode 11


Problem statement

You are given an array height, where each element represents 
the height of a vertical line.

Choose two lines that, together with the x-axis, form a 
container that holds the maximum amount of water.

Return the maximum water area.

The rule is:
- If height[left] < height[right], move left += 1.
- If height[left] > height[right], move right -= 1.
- If both heights are equal, either pointer can move.
'''
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

def max_area(height):
    left = 0 
    right = len(height) - 1
    max_area = float('-inf')

    while left < right:
        area = min(height[left], height[right]) * (right - left)
        max_area = max(area, max_area)

        if height[left] < height[right]:
            left += 1 
        else:
            right -= 1 

    return max_area      


print(max_area(height))

'''
Complexity	    Value
Time	        O(n)
Auxiliary space	O(1)
'''