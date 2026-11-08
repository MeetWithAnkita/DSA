arr = [2, 4, 6, 8, 10]

left = 0
right = len(arr) - 1 

while left < right:
    print( arr[left], arr[right] )
    left += 1 
    right -= 1


'''
Pattern	                Typical use
----------------------------------------------------
Opposite direction	    Pair sum in sorted array
Same direction	        Remove duplicates
Fast and slow pointers	Cycle detection
Two arrays	            Merge sorted arrays
In-place modification	Move zeros
'''