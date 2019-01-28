# OOP Tutorial from
# https://www.youtube.com/watch?v=BJ-VvGyQxho&index=2&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc
import datetime
class Employee:
    #Class Variables
    raise_amount = 1.04
    num_of_emps = 0
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first+'.'+last+'@avengers.com'
        self.pay = pay
        Employee.num_of_emps +=1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_gen_raise(cls,amount):
        cls.raise_amount = amount
    # classmethods are usually used as optional creators. in other
    # words, they give people more options for how to create an
    # instance of the calls
    # In other words, people use classmethods as alternative
    # constructors

    @classmethod
    def from_strings(cls, some_string):
        first, last, pay = some_string.split('-')
        return cls(first,last,pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    ## magic methods
    def __add__(self, employee):
        return self.pay + employee.pay


### End of class Employee
print(" ########################## Part 1 #########################")
emp_1 = Employee('Tony', 'Stark', 100000)
emp_2 = Employee('Steve', 'Rogers', 45000)
emp_3 = Employee('Bruce', 'Banner', 60000)
emp_4 = Employee('Peter', 'Parker', 5000)

print(emp_2.fullname()+" Gets a raise for being the Captain")
emp_2.apply_raise()
print(emp_2.fullname()+": "+str(emp_2.pay))

#Now, everybody gets a raise of 10%
Employee.raise_amount = 1.1
#But, Tony Stark gets a raise of 20%
print(emp_1.fullname()+" Previous Salary = "+str(emp_1.pay))
emp_1.raise_amount=1.20
emp_1.apply_raise()
print(emp_1.fullname()+" New Salary = "+str(emp_1.pay))
emp_2.apply_raise()
print(emp_2.fullname()+" New Salary = "+str(emp_2.pay))
emp_3.apply_raise()
emp_4.apply_raise()

print("Number of Employees: ")
print(Employee.num_of_emps)
print("Current Raise: ")
print("General amount: "+str(Employee.raise_amount))
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(emp_3.raise_amount)
print(emp_4.raise_amount)
print("New Raise Amounts")
Employee.set_gen_raise(1.15)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(emp_3.raise_amount)
print(emp_4.raise_amount)

print(" ########################## Part 2 #########################")
emp_str_a = 'clark-kent-10000'
emp_str_b = 'bruce-wayne-10000'

emp_b = Employee.from_strings(emp_str_a)
emp_a = Employee.from_strings(emp_str_b)
print(emp_a.fullname()+" is Superman")
print(emp_b.fullname()+" is Batman")


print(" ########################## Part 3 #########################")
my_date = datetime.date(2016,7,10)
print(Employee.is_workday(my_date))
my_date2 = datetime.date(2016,7,11)
print(Employee.is_workday(my_date2))



print(" ########################## Part 4 #########################")

class SuperHero(Employee):
    good = True
    def __init__(self, first, last, pay, superPower):
        super().__init__(first,last,pay)
        self.superPower = superPower

class Boss(Employee):
    def __init__(self, first, last, pay, employees = None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    def add_emp(self,emp):
            if emp not in self.employees:
                self.employees.append(emp)
    def rem_emp(self,emp):
        if emp not in self.employees:
            self.employees.remove(emp)
    def print_emp(self):
        for emp in self.employees:
            print('-->', emp.fullname())

emp_5 = SuperHero('Prince', 'Tachala', 123020,'Has a lot of vibranium')
leader1 = Boss('Nick','Fury', 120000, [emp_1,emp_2])
print(leader1.email)
leader1.print_emp()
leader1.print_emp()
leader1.add_emp(emp_3)
leader1.rem_emp(emp_1)
print(isinstance(leader1, Employee))
print(isinstance(leader1, Boss))
print(issubclass(SuperHero, Employee))
print(help(SuperHero))
print(emp_5.__dict__)

print(" ########################## Part 5 #########################")
print("Magic Methods")

class Supervillain():
    def __init__(self, fname,lname, superpower):
        self.fname = fname
        self.lname = lname
        self.superpower = superpower

    @property
    def fullname(self):
        return self.fname+' '+self.lname

    @property
    def email(self):
        return self.fname+'.'+self.lname+'@email.com'

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.fname = first
        self.lname = last
    @fullname.deleter
    def fullname(self):
        print(self.fname+' '+self.lname+' Delete Name!')
        self.fname = None
        self.lname = None

    def say(self):
        return "I hate superheros"
    def __repr__(self):
        return 'Supervillain({},{},{})'.format(self.fname, self.lname,self.superpower)
        #meant for the programers, its an unambiguous representation of the object.
    def __str__(self):
        # meant to be for the end user
        return '{} - {}'.format(self.fullname,self.superpower)

venom = Supervillain('Eddie','Brock','Symbiote')
print(venom)
print(venom.__str__())
print(venom.__repr__())
print(emp_2+emp_1)
print(venom.fullname)
print(venom.email)
venom.fullname = 'someone else'
print(venom.fullname)
del venom.fullname
print(venom.__dict__)




