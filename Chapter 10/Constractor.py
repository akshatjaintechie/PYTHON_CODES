class employee:
    salary = 1200000
    age = 20
    language = "Python"


    def __init__(self,salary, age, language):
        self.salary = salary
        self.age = age
        self.language = language
        print("the akshat is greatest footballer in the  world")

    def getinfo(self):
        print(f"salary of the employee {self.salary} and age of the employee is {self.age}"
              f" and language used in the code is {self.language}")

    @staticmethod
    def greet():
        print("the great akshat jain is coming inside")

harry = employee(1300000, 21 ,"Python")
print(harry.salary, harry.age, harry.language)
# harry.getinfo()
# harry.greet()