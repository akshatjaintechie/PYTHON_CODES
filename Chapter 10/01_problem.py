class Programmers:
    Company = "Microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin
    
p = Programmers("Akshat", 1200000, 250606)
print(p.name , p.salary, p.pin, p.Company)

r = Programmers("Rohan", 1200000, 250606)
print(r.name , r.salary, r.pin, r.Company)