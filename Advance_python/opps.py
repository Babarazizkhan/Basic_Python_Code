# using opps creating student record
# class blueprint template 
# class student:
#     def __init__(self, name, grade, percentage):  # method 
#         self.name = name      # attribute 
#         self.grade = grade   # attribute 
#         self.percentage = percentage # attribute 
    
#     def student_detail(self):
#         print(f'{self.name}, is in class {self.grade}, is % {self.percentage}')
    
#     # object instance of class 
# student1 = student('babar', 12, 78)
# student2 = student('Basit ', 54, 12)
# student3 = student('kasfi', 18, 80)

# print(f'{student1.name},{student1.grade},{student1.percentage}')
# print(f'{student2.name},{student2.grade},{student2.percentage}')
# print(f'{student3.name},{student3.grade},{student3.percentage}')

# print(student1.__dict__)
# print(student2.__dict__)
# print(student3.__dict__)

# student1.student_detail()
# student2.student_detail()
# student3.student_detail()

# modify the vlue 
# student1.percentage = 45
# student1.student_detail()

# del the parameter 
# del student1.percentage
# print(student1.__dict__)

# delete object
# del student1
# print(student1)

# project task

class bankacount():
    def set_detail(self, name, balance=0):
        self.name = name
        self.balance = balance

    def display(self):
        print(self.name, self.balance)

    def withdraw(self, amount):
        self.balance -= amount
    
    def deposit(self, amount):
        self.balance += amount


# inintilze the object

object1= bankacount()
object1.set_detail('babar', 500)

object2 = bankacount()
object2.set_detail('moiz')

object1.display()
object2.display()

object1.withdraw(100)
object1.deposit(300)

object1.display()
object2.display()