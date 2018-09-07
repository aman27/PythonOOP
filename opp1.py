#python object oriented program

class Employee:

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
