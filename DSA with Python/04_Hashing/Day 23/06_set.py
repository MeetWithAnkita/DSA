nums = {10, 20, 30}
nums.add(40)
nums.add(20)

print(nums)

'''
A Python set is unordered, so it does not guarantee that 
elements will appear in insertion order.

Remember the difference
Data structure	Maintains insertion order?
List	        Yes
Tuple	        Yes
Dictionary	    Yes (Python 3.7+)
Set	            No

Important: add() doesn't mean add at the front or end. 
It simply inserts an element into the set.
'''


nums.remove(20)
print(nums)

nums.discard(30)
print(nums)

nums.discard(50)
print(nums)

'''
Method	    If element doesn't exist
remove()	Raises KeyError
discard()	Does nothing

discard() , if element in set, remove, else: do Nothing
'''

print(20 in nums)
print(40 in nums)


'''
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
Union — all unique elements

A | B
Output
{1, 2, 3, 4, 5, 6}

Intersection — common elements

A & B
Output
{3, 4}

Difference — elements in A but not B

A - B
Output
{1, 2}

Symmetric Difference — elements not common to both

A ^ B
Output
{1, 2, 5, 6}
'''