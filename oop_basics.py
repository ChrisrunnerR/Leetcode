class Pet: # generalizaio
    def __init__(self, name, age):
        self.name = name
        self.age = age 
    
    def show(self):
        print(f"I am {self.name} an I am {self.age} years old")


class Cat(Pet): 
    # if you want to add in another attribute 

    def __init__(self, name, age , color):
        super().__init__(name, age)
        self.color = color 
    def speak(self):
        print("Meow")

    def show(self):
        print(f"I am {self.name} an I am {self.age} years old w color: {self.color}")

class Dog(Pet):

    def speak(self):
        print("Bark")




p = Pet("ch", 20)
p.show()


c = Cat("Bill", 30, "blue")
c.show()
