class Employee:
    def __init__(self,name,eno,salary):
     self.__name=name
     self.eno=eno
     self._salary=salary

    def setName(self,name):
        self.__name=name

    def getName(self):
        return self.__name

    def display(self):
        print(f"Name:{self.__name}\nEno:{self.eno}\nSalary:{self._salary}")

class Allowance(Employee):
    def __init__(self,name,eno,salary,da,hra):
        super().__init__(name,eno,salary)
        self.__da=da
        self.__hra=hra
        self.__gross=0

    def cal_salary(self):
        self.__da = (self._salary*self.__da)/100
        self.__hra = (self._salary*self.__hra)/100
        self.__gross = self._salary+self.__da+self.__hra

    def display(self):
        super().display()
        print(f"DA:{self.__da}")
        print(f"HRA:{self.__hra}")
        print(f"GROSS:{self.__gross}")

name=input("Enter the employee name:")
eno=int(input("Enter the employee number:"))
salary=int(input("Enter the salary:"))
da=int(input("Enter the DA(%):"))
hra=int(input("Enter the HRA(%):"))
a=Allowance(name,eno,salary,da,hra)
a.cal_salary()
a.display()
print("********")
print("Employee Name:",a.getName())
change=input("Do you want to change name?(y/n)")
if change=='y' or change=='Y':
    newname=input("Enter new name:")
    a.setName(newname)
    print("Name Updated Successfully")
    a.display()
else:
    print("Thank you")

#Shorter Version
'''class Employee:
    def __init__(self, name, eno, salary):
        self.__name = name
        self.eno = eno
        self._salary = salary

    def set_name(self, name): 
        self.__name = name
    def get_name(self): 
        return self.__name
    def display(self): 
        print(f"Name: {self.__name}, No: {self.eno}, Salary: {self._salary}")

class Allowance(Employee):
    def __init__(self, name, eno, salary, da, hra):
        super().__init__(name, eno, salary)
        self.gross = salary + salary*da/100 + salary*hra/100

    def display(self):
        super().display()
        print("Gross:", self.gross)

a = Allowance(input("Name: "), int(input("No: ")), float(input("Salary: ")),
              float(input("DA%: ")), float(input("HRA%: ")))
a.display()

if input("Change name? (y/n): ").lower() == 'y':
    a.set_name(input("New name: "))
    a.display()
'''
