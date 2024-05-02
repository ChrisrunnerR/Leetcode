class Person:

    num_of_people = 0

    def __init__(self,name):
        self.name = name
        Person.add_person()

    # class method 
    # do not have access to any instance 
    # act on the class itself
    @classmethod
    def number_of_people_(cls):
        return cls.num_of_people
    
    @classmethod
    def add_person(cls):
        cls.num_of_people +=1
    



p1 = Person("chris")
p2 = Person("Tim")

print(Person.number_of_people_())
#print(Person.num_of_people)


