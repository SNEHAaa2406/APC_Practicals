class Student:

    # Constructor
    def __init__(self, name, roll_no, marks1, marks2, marks3):
        self.name = name
        self.roll_no = roll_no
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3

        print("Student object created")

    # Calculate total
    def calculate_total(self):
        return self.marks1 + self.marks2 + self.marks3

    # Check Pass or Fail
    def check_result(self):
        total = self.calculate_total()

        if self.marks1 >= 35 and self.marks2 >= 35 and self.marks3 >= 35:
            return "PASS"
        else:
            return "FAIL"

    # Display details
    def display(self):
        total = self.calculate_total()

        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Marks:", self.marks1, self.marks2, self.marks3)
        print("Total:", total)
        print("Result:", self.check_result())

    # Destructor
    def __del__(self):
        print("Student object destroyed")


# Create student objects
student1 = Student("Sneha", 101, 80, 75, 90)
student2 = Student("Rahul", 102, 80, 30, 70)

# Display details
student1.display()
print()

student2.display()

# Destroy objects
del student1
del student2