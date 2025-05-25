class Calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"the square is {self.n*self.n}")

    def  Cube(self):
        print(f"the cube is {self.n*self.n*self.n}")

    @staticmethod
    def hello():
        print("hello there")

a =Calculator (4)
a.square()
a.Cube()
a.hello()