# names = []
# grades = []

# while True:

#     print("\n1. Add student")
#     print("2. Update grade")
#     print("3. Remove student")
#     print("4. Calculate average")
#     print("5. Show highest and lowest")
#     print("6. Exit")

#     choice = int(input("Enter your choice: "))

    
#     if choice == 1:
#         name = input("Enter student name: ")
#         grade = int(input("Enter grade: "))

#         names.append(name)
#         grades.append(grade)

#         print("Student added successfully!")

    
#     elif choice == 2:
#         name = input("Enter student name: ")

#         if name in names:
#             index = names.index(name)

#             new_grade = int(input("Enter new grade: "))
#             grades[index] = new_grade

#             print("Grade updated!")
#         else:
#             print("Student not found!")

    
#     elif choice == 3:
#         name = input("Enter student name: ")

#         if name in names:
#             index = names.index(name)

#             names.pop(index)
#             grades.pop(index)

#             print("Student removed!")
#         else:
#             print("Student not found!")

    
#     elif choice == 4:
#         if len(grades) == 0:
#             print("No grades available!")
#         else:
#             average = sum(grades) / len(grades)
#             print("Average grade:", average)

    
#     elif choice == 5:
#         if len(grades) == 0:
#             print("No grades available!")
#         else:
#             print("Highest grade:", max(grades))
#             print("Lowest grade:", min(grades))

#     # Exit
#     elif choice == 6:
#         print("Program ended.")
#         break

#     else:
#         print("Invalid choice!")

# project1 = {"Amit", "Sneha", "Rahul", "Priya", "Neha"}
# project2 = {"Rahul", "Priya", "Karan", "Neha", "Riya"}

# # Employees working on both projects
# print("Employees in both projects:", project1 & project2)

# # Employees only in Project 1
# print("Only in Project 1:", project1 - project2)

# # Employees only in Project 2
# print("Only in Project 2:", project2 - project1)

# # Total unique employees
# print("Total unique employees:", project1 | project2)

# server_ip = ("192.168.1.10",)
# allowed_ips = ["192.168.1.1", "192.168.1.2"]


# def update_allowed_ips():
#     new_ip = input("Enter new allowed IP: ")
#     allowed_ips.append(new_ip)
#     print("IP added successfully")


# while True:
#     print("\n1. Add allowed IP")
#     print("2. Change server IP")
#     print("3. Display configuration")
#     print("4. Exit")

#     choice = int(input("Enter your choice: "))

#     if choice == 1:
#         update_allowed_ips()

#     elif choice == 2:
#         print("Server IP cannot be changed")

#     elif choice == 3:
#         print("Server IP:", server_ip)
#         print("Allowed IPs:", allowed_ips)

#     elif choice == 4:
#         print("Program ended")
#         break

#     else:
#         print("Invalid choice")