class Demo:
    a = 4

o = Demo()
print(o.a) #print the class attribute because instanse attribute is not present   

o.a = 0 #intance attribute is set
print(o.a) #prints the class attribute because instance attribute is present

print(Demo.a) 