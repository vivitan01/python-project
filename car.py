class car:
    def __init__(self,color, yom):
        self.color =color
        self.yom =yom


    def drive(self):
        print("You drive",self.color,"car")

car1 = car("black",2009)
print(car1.color)
car1.drive()

car2 = car("blue",2002)
print(car2.color)
car2.drive()