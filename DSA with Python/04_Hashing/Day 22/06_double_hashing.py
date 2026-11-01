'''
What is Double Hashing?
Double Hashing uses two different hash functions to find the next available position when a collision occurs.

Instead of moving by 1 or by squares, the second hash function determines the jump size.
Formula: 

j = (h_1(key) + i * h_2(key)) % m


Where:
- h_1(key) = First hash function (original index).
- h_2(key) = Second hash function (jump size).
- i = Attempt number.
- m = Hash table size.
'''

size = 7
keys = [10, 17, 24, 31]

def double_hashing(size, keys):
    table = [None] * size
    def index(key):
        h1_k = key % size 
        R = 5 # as size = 7 so , r = 5 , bcz 5 is less then 7 also a prime number 
        h2_key = R - (key % R)

        for i in range(size):
            j = (h1_k + (i * h2_key)) % size
            if table[j] == None:
                table[j] = key
                break

    for i in keys:
        index(i)

    return table 


print(double_hashing(size, keys))


# Operation	            Complexity
# ==========================================
# Best-case insertion	O(1)
# Worst-case insertion	O(m)
# Building table	    O(n × m) worst case
# Space	                O(m)
