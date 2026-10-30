student = {
    "name": "Sneha",
    "age": 20,
    "branch": "CSE",
    "year": 3
}
print(student)
print(student["name"])
print(student["age"])



student = {
    "name": "Sneha",
    "age": 20
}
student["city"] = "Pune"
student["age"] = 21
del student["city"]
print(student)
 

student = {
    "name": "Sneha",
    "age": 20,
    "branch": "CSE"
}
for key, value in student.items():
    print(key, ":", value)



    marks = {
    "Python": 85,
    "SQL": 90,
    "Statistics": 78,
    "Excel": 88
}
print("Number of subjects:", len(marks))




marks = {
    "Python": 85,
    "SQL": 90,
    "Statistics": 78
}
total = 0
for mark in marks.values():
    total += mark
print("Total marks:", total)



text = "banana"
frequency = {}
for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1
print(frequency)