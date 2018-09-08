#python object oriented program

#class Employee():  #python version 3 compatoble
class Employee(object):

	num_of_emps = 0

	raise_amt = 1.04

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@company.com'

		Employee.num_of_emps += 1

	def fullname(self):
		return '{} {}'.format(self.first, self.last)

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amt)	


	@classmethod
	def set_raise_amt(cls, amount):
		cls.raise_amt = amount		

	@classmethod
	def from_string(cls, emp_str):
		first, last, pay = emp_str.split('-')
		return cls(first, last, pay)	

	@staticmethod
	def is_workday(day):
		if day.weekday() == 5 or day.weekday() == 6:
			return False
		return True	

	def __repr__(self):
		return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)	

	def __str__(self):
		return "{} - {}".format(self.fullname(), self.email)

	def __add__(self, other):
		return self.pay + other.pay

	def __len__(self):
		return len(self.fullname())		

class Developer(Employee):
	raise_amt = 1.10
	def __init__(self, first, last, pay, prog_lang):
		#super().__init__(first, last, pay).  #python version 3 compatoble
		super(Developer, self).__init__(first, last, pay)
		self.prog_lang = prog_lang

class Manager(Employee):
	
	def __init__(self, first, last, pay, employees = None):
		#super().__init__(first, last, pay)  #python version 3 compatoble
		super(Manager, self).__init__(first, last, pay)
		if employees == None:
			self.employees = []
		else:
			self.employees = employees		

	def add_emp(self, emp):
		if emp not in self.employees:
			self.employees.append(emp)

	def remove_emp(self, emp):
		if emp in self.employees:
			self.employees.remove(emp)		


	def print_emp(self):
		for emp in self.employees:
			print ('-->', emp.fullname())		
			
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

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

print(emp_1.__dict__)
print(Employee.__dict__)

emp_1.raise_amt = 1.05
print(emp_1.__dict__)
print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

Employee.raise_amt = 1.06
print(emp_1.__dict__)
print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

Employee.set_raise_amt(1.07)
print(emp_1.__dict__)
print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

emp_str_1 = 'manoj-kumar-70000'
emp_str_2 = 'kunal-kapoor-30000'
emp_str_3 = 'rachita-singh-90000'

'''
first, last, pay = emp_str_1.split('-')
new_emp_1 = Employee(first, last, pay)
'''
new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)

import datetime
my_date = datetime.date(2016, 7, 10)

print(Employee.is_workday(my_date))

print(help(Developer))

dev_1 = Developer('Amani', 'Yadav', 50000, 'python')
dev_2 = Developer('Test', 'Employee', 70000, 'java')

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

print(dev_1.prog_lang)

mgr_1 = Manager('Amit', 'Garg', 90000, [dev_1])

mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_1)

mgr_1.print_emp()

print(isinstance(mgr_1, Manager))
print(isinstance(mgr_1, Employee))
print(isinstance(mgr_1, Developer))
print(issubclass(Developer, Employee))
print(issubclass(Manager, Employee))
print(issubclass(Developer, Manager))

print(emp_1)

print(repr(emp_1))
print(str(emp_1))

print(emp_1.__repr__())
print(emp_1.__str__())

print(emp_1 + emp_2)

print(len(emp_1))
