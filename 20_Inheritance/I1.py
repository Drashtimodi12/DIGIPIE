# Single Inheritance – Employee & Manager
# Requirements:
# Create class Employee
# method: work() → print “Employee works.”
# Create class Manager(Employee)
# method: manage() → print “Manager manages team.”
# Create object of Manager and access both methods.

class Employee:
    def work(self):
        a = input("Enter Your Work you do in company: ")
        print(a)

class Manager(Employee):
    def manage(self):
        print(f"Manager mange {Employee.a} employee work based salary.")

m = Manager()
m.work()
m.manage()