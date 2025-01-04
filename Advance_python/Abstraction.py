# Abstraction "hiding uncessery data from users through class and method"
# connect vriable with  objects
class student:
    def __init__(self, name, grade, percentage, team):  # method 
        self.name = name      # attribute 
        self.grade = grade    # attribute 
        self.__percentage = percentage # attribute # double underscore limit the acess mean no one can modirfy the percentage without you 
        self.team = team  # attribute 
    def student_detail(self):      # we add the +2 in percenatage is called abstraction 
        print(f'{self.name}, is in class {self.grade}, is % {self.percentage+2},{self.team}')
    
    def get_percentage(self):
        return self.__percentage


team1 = 'A'     # This is the variable which i add in the 
team2 = 'B'     # student class and also add in the object
team3 = 'C'        
    
# object instance of class 
student1 = student('babar', 12, 78, team1)
student2 = student('Basit ', 54, 12, team2)
student3 = student('kasfi', 18, 80, team3)

# student1.student_detail()
# student2.student_detail()
# student3.student_detail()

print(student1.get_percentage()) 
print(student2.get_percentage())

