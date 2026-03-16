from abc import ABC, abstractmethod

# a) Create an abstract class called Employee
class Employee(ABC):
    def __init__(self, name, salary):
        # Private attributes (Encapsulation)
        self.__name = name
        self.__salary = salary

    # Getter methods to access private attributes
    def get_name(self):
        return self.__name

    def get_salary(self):
        return self.__salary

    def display_info(self):
        print(f"Employee Name: {self.__name}")

    @abstractmethod
    def calculate_salary(self):
        pass

# b) Create two child classes
class FullTimeEmployee(Employee):
    # c) Implement calculate_salary (Polymorphism)
    def calculate_salary(self):
        return self.get_salary()

class PartTimeEmployee(Employee):
    # c) Implement calculate_salary (Polymorphism)
    def calculate_salary(self):
        return self.get_salary() / 2

# d) Write a Python program to demonstrate
if __name__ == "__main__":
    ft_emp = FullTimeEmployee("Alice", 60000)
    pt_emp = PartTimeEmployee("Bob", 40000)

    employees = [ft_emp, pt_emp]

    for emp in employees:
        emp.display_info()
        print(f"Calculated Salary: ${emp.calculate_salary()}")
        print("-" * 20)