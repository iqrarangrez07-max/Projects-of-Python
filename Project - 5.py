# OOP Wrapper :

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("Person Details :")
        print("Name :", self.name)
        print("Age :", self.age)
class Employee(Person):
    def __init__(self,name=" ",age=0,employee_id=" ",salary=0.0):
        super().__init__(name,age)
        self.__employee_id=employee_id
        self.__salary=salary
    def get_employee_id(self):
        return self.__employee_id
    def get_salary(self):
        return self.__salary
    def set_employee_id(self,emp_id):
         self.__employee_id=emp_id
    def set_salary(self,salary):
        self.__salary=salary
    def display(self):
        print("Employee Details :")
        print("Name :", self.name)
        print("Age :", self.age)
        print("Employee ID :", self.__employee_id)
        print("Salary :", self.__salary)
    def __del__(self):
        print("All resources have been freed.")
class Manager(Employee):
    def __init__(self,name,age,employee_id,salary,department):
        super().__init__(name,age,employee_id,salary)
        self.department=department
    def diaplay(self):
        print("Manager Details :")
        print("Name :", self.name) 
        print("Age :", self.age) 
        print("Employee ID :", self.get_employee_id()) 
        print("Salary :", self.get_salary())
        print("Department :", self.department)

person_x=None
employee_x=None
manager_x=None
while True :
    print("--- Python OOP Project: Employee Management System ---")
    print()
    print("Choose an operation")
    print("1. Create a Person")
    print("2. Create an Employee")
    print("3. Create a Manager")
    print("4. Shoe Details")
    print("5. Exit")
    print()
    choice=input("Enter your choice : ")
    print()
    if choice =="1":
        name=input("Enter Name : ")
        age=int(input("Enter Age : "))
        person_x=Person(name,age)
        print()
        print("Person created with name :", name, "and age :", age)
        print()
    elif choice =="2":
        name=input("Enter Name : ")
        age=int(input("Enter Age : "))
        emp_id=input("Enter Employee ID : ")
        salary=float(input("Enter Salary : "))
        employee_x=Employee(name,age,emp_id,salary)
        print()
        print("Employee created with name :", name, ", age :", age, ", ID :", emp_id, ", and salary :", salary)
        print()
    elif choice=="3":
        name=input("Enter Name : ")
        age=int(input("Enter Age : "))
        emp_id=input("Enter Employee ID : ")
        salary=float(input("Enter Salary : "))
        dept=input("Entr Department : ")
        manager_x=Manager(name,age,emp_id,salary,dept)
        print()
        print("Manager created with name :", name, ", age :", age, ", ID :", emp_id, ", salary :", salary, ", and department :", dept)
        print()
    elif choice=="4":
        print("Choose details to show :")
        print("1. Person")
        print("2. Employee")
        print("3. Manager")
        show=input("Enter your choice : ")
        print()
        if show=="1" and person_x:
            person_x.display()
            print()
        elif show=="2" and employee_x:
            employee_x.display()
            print()
        elif show=="3" and manager_x:
            manager_x.display()
            print()
        else :
            print("No data available")
            print()
    elif choice=="5":
        print("Exiting the system. All resources have been freed.")
        print()
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Try again.")

print("Is Manager subclass of Employee?", issubclass(Manager,Employee))