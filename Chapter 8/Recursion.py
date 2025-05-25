def Factorial(n):
    if(n==1 or n==0):
        return 1
    return n * Factorial(n-1)


n = int(input("enter a number: "))
print(f"the factorial of {n} is {Factorial(n)}")