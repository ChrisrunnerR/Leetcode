
class Person:

    def __init__(self, name, age, weight):
        self.name = name
        self.age = age 
        self.weight = weight
    

    def viewData(self):
        print(f"My name is {self.name} I am {self.age} years old and weigh {self.weight}")

    

class Student(Person):
    
    def __init__(self, name, age, weight, grade):
        super().__init__(name, age, weight)
        self.grade = grade 

    def viewData(self):
        print(f"My name is {self.name} I am {self.age} years old and weigh {self.weight} pounds \
and I am in grade {self.grade}")
        
 
#  '''  You've effectively used the super() function to initialize the inherited attributes 
#    (name, age, and weight), which is a standard practice in Python for ensuring that the 
#    initialization logic in the parent class is preserved.'''

s1 = Student("chris", 12, 125, 12)
s1.viewData() 