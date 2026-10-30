class Person:

    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Display person information
    def display_person_info(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Employee(Person):

    # Constructor
    def __init__(self, name, age, employee_id, salary):

        # Calling parent class constructor
        super().__init__(name, age)

        self.employee_id = employee_id
        self.salary = salary

    # Display employee information
    def display_employee_info(self):

        # Calling parent class method
        self.display_person_info()

        print("Employee ID:", self.employee_id)
        print("Salary:", self.salary)


# Creating Employee object
employee1 = Employee("Sneha", 20, 101, 50000)

# Display employee details
employee1.display_employee_info()