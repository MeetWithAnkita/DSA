'''
Method	           Operator	Purpose
union()	                |	Combine elements
intersection()	        &	Find common elements
difference()	        -	Find elements in first set only
symmetric_difference()	^	Find elements not common
issubset()	            —	Check whether one set is contained in another
isdisjoint()	        —	Check whether two sets have no common elements
'''
A = {1, 2, 3}
B = {3, 4, 5}
print(A | B)
print(A.union(B))
print(A.intersection(B))
print(A.isdisjoint(B))
print(A.issubset(B))
print(A.symmetric_difference(B))
print(A.difference(B))
print(B.difference(A))