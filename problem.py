
# what if not int 
# what if not 3 

import math 

class Shape:

    def __init__(self, base, height , sides=0 ):

        self.base = base
        self.height = height 
        self.sides = sides

    def calculateArea(self):
        pass 


class Triangle(Shape):


    def calculateArea(self):
        area = self.base * self.height

        print(area)

        
class Square(Shape):

    def calculateArea(self):
        area = self.sides * self.sides 

class Circle():

    def __init__(self, radius):
        self.radius = radius 

    def calculateArea(self):
        area = (self.radius * self.radius) *  math.pi
        return area
        


def main():
    print("Hello, what shape would you like to calculate the area for?")
    print("Choose from options below:")
    
    while True:
        choice = input("1) Square \n2) Circle \n3) Triangle \n0) Exit \n")

        if choice == "0":
            print("Exiting program.")
            break
        elif choice == "1":
            print("Let's calculate the area of a square.")
        elif choice == "2":
            print("Let's calculate the area of a circle.")
        elif choice == "3":
            print("Let's calculate the area of a triangle.")
            radius = input("What is the radius of your circle?\n") 
            radius = int(radius)
            c1 = Circle(radius)
            print(f"The area of your circle is {c1.calculateArea()}")
        else:
            print("Invalid choice, please enter 1, 2, 3, or 0 to exit.")
            continue

# Call the main function
main()

           
       
       






if __name__ == "__main__":
   main()
   
   

       



    

    

