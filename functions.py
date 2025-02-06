#built-in Functions
y = max(56, 75,23, 18,24)
print("The maximumum value is",y)

x = min(6, 34,15,97)
print("The minimum value is", x)

# user-defined functions
def name():
    print("Millicent")
name() #This is calling a function

def product():
    a =10
    b = 20
    print(a * b)
product()

# Parameter/ variable and argument/value

def sum(num1 ,num2):

    print(num1 + num2)
sum(5 ,6)
sum(10 ,20)
sum(54 ,15)

def Employee(name, age, position, salary):

    print(name, age, position,salary)

Employee("millicent", 21 ,"CEO",56000)
Employee("Faith", 24 ,"Clerk",470000)
Employee("Mark", 35 ,"receiptionist",39000)
Employee("Japheth", 28 ,"managing director",50000)


#A program to display details of 5 students
#full name, age, course, gender,nationality

def students(fullname ,age, course, gender, nationality):
     print(fullname,age,course,gender,nationality)

students("Benard mwangi",25,"MIT","Male","Kenyan")
students("Fiancy AJ",30,"Nursing","Female","American")
students("Rael clinton",35,"Data science","Male","swiss")
students("Rayan Aisha",45,"Education","Female","Ethiopian")
students("Cris kelsey",38,"Cybersecurity","Male","Tanzanian")