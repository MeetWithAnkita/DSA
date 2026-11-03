student = {
    "name": "Ankita",
    "age": 24,
    "course": "MCA"
}

print(student["name"])
print(student.get("city", "Not Found"))
print(student.get("age", "Not Found"))

student["city"] = "Midnapore"
student["age"] = 23
print(student)


'''
Method	    Purpose
==============================================
get(key)	Returns the value of a key
keys()	    Returns all keys
values()	Returns all values
items()	    Returns key-value pairs
update()	Adds or updates multiple entries
pop(key)	Removes a key and returns its value
clear()	    Removes all entries
'''