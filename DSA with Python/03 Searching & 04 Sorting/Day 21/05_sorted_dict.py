employees = [
    {"name": "Ankita", "salary": 25000},
    {"name": "Riya", "salary": 35000},
    {"name": "Priya", "salary": 20000}
]

results = sorted(employees, key = lambda x: x["salary"])

print(results)