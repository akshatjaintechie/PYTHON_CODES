a = int(input("enter a age: "))

#if elif else ladder

if(a>18):
    print("you are above the age of consent")
elif(a<0):
    print("you are entering an invalid age")
elif(a==0):
    print("you have entered zero which is not a valid age")
else:
    print("you are below the age of consent")
    
print("end of Program")