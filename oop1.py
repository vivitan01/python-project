class person:
    def __init__(self,name,gender,age):
        self.name = name
        self.gender = gender
        self.age = age


    def detail(self):
         print(self.name,"is a",self.gender)

teacher = person("Joe","Male",45)
teacher.detail()
print(teacher.name)


accountant =person("Mary","Female",43)
accountant.detail()
print(accountant.name)
