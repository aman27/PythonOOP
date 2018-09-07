#python object oriented program

class Employee:

	num_of_emps = 0

	raise_ammount = 1.04

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@company.com'

		Employee.num_of_emps += 1

	def fullname(self):
		return '{} {}'.format(self.first, self.last)

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_ammount)		

print(Employee.num_of_emps)		

emp_1 = Employee('Aman', 'Yadav', 50000)
emp_2 = Employee('Test', 'User', 60000)

print(Employee.num_of_emps)	

"""
print(emp_1)
print(emp_2)	

emp_1.first = "Aman"
emp_1.last = "Yadav"
emp_1.email = "Aman.Yadav@company.com" 
emp_1.pay = 50000


emp_2.first = "Test"
emp_2.last = "User"
emp_2.email = "Test.User@company.com" 
emp_2.pay = 60000
""" 

print(emp_1.email)
print(emp_2.email)

#print('{} {}'.format(emp_1.first, emp_1.last))

print(emp_1.fullname())
print(Employee.fullname(emp_1))

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

print(Employee.raise_ammount)
print(emp_1.raise_ammount)
print(emp_2.raise_ammount)

print(emp_1.__dict__)
print(Employee.__dict__)

emp_1.raise_ammount = 1.05
print(emp_1.__dict__)
print(Employee.raise_ammount)
print(emp_1.raise_ammount)
print(emp_2.raise_ammount)



