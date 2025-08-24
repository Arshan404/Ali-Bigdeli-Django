class Employee:
    salary = 3000

    def __init__(self , fname , lname):
        self.fname = fname
        self.lname = lname

    def get_full_name(self):
        return f"{self.fname} {self.lname}"
    
emp1 = Employee("Ali" , "Bigdeli")
print("Full name : " ,emp1.get_full_name())
print("salary : " , Employee.salary , "USD")
        