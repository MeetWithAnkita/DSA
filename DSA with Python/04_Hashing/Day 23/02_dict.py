'''
Method	    Purpose
===============================================
get(key)	Returns the value of a key
keys()	    Returns all keys
values()	Returns all values
items()	    Returns key-value pairs
update()	Adds or updates multiple entries
pop(key)	Removes a key and returns its value
clear()	    Removes all entries
'''

student = {"name": "Ankita", "age": 24}

for k, v in student.items():
    print(k, v)

print(student.keys())
print(student.values())
print(student.items())
print(student.pop("age"))
print(student)
print(student.get("age", "Not Found"))
print(student.clear())
print(student)