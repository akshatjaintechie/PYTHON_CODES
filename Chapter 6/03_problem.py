marks1= int(input("enter marks of subject: "))
marks2= int(input("enter marks of subject: "))
marks3= int(input("enter marks of subject: "))
marks4= int(input("enter marks of subject: "))

total_percentage = (100*(marks1 + marks2 + marks3 + marks4))/300

if(total_percentage>=40):
    print("you are passed:", total_percentage)

else:
    print("you are failed, try again next time!", total_percentage)