class employee:
    salary = 1200000
    age = 20
    language = "Python"

    def getinfo(self):
        print(f"salary of the employee {self.salary} and age of the employee is {self.age}"
              f" and language used in the code is {self.language}")

    @staticmethod
    def greet():
        print("the great akshat jain is coming inside")

harry = employee()

harry.getinfo()
harry.greet()