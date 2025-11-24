import math
positive_infinity = math.inf
negative_infinity = -math.inf
def Arithmatic_operations():
    print("Press 1 for +")
    print("Press 2 for -")
    print("Press 3 for *")
    print("Press 4 for /")
    print("Press 5 for //")
    n = int(input("input any number of above choices: "))   
    a = float(input("Enter first number: "))
    b = float(input("Enter another number: ")) 
    if n == 1:
        print(f"The sum of {a} and {b} is",a + b )
    elif n==2:
         print(f"The substraction of {a} and {b} is", a - b)
    elif n==3:
         print(f"The product of {a} and {b} is",a*b)
    elif n==4:
         print(f"The division of {a} and {b} is", a/b)
    elif n==5 :
         print( f"The floor division of {a} and {b} is",a//b)
    else :
         print("Your entered integer is invalid.")



     
def Trigonometric_calculations():
    r = input(" Enter trigonometric function and angle in radian : ")
    e = float(input(" Enter an angle: "))
    
    rad = math.radians(e)
    
    if r == "sin":
        print(math.sin(rad))
    elif r == "cos":
         print(math.cos(rad))
    elif r == "tan":
         print(math.tan(rad))
    elif r == "cot":
         print(1/math.tan(rad))
    elif r=="sec":
         print(1/math.cos(rad))
    elif r=="cosec":
         print(1/math.sin(rad))
    else:
        print("Invalid input!")

def exponential_and_logarithmic_functions():
     u = input("Enter any number or type log if you want to perform logarithmic function : ")
     if u== "log":
          s = float(input("Input number: "))
          print(math.log10(s))
     elif negative_infinity < u < positive_infinity :
          v = float(input(f"{u} raises to: "))
          print(u**v)
     else:
          print("Invalid input!")
          
    
print("Choose which type of operation you want to perform ")

def Calculator():
    print("Enter 'A' for Arithmatic operation")
    print("Enter 'T' for Trigonometric function")
    print("Enter 'E' for exponential and logarithmic function")
    I = input()

    if I == "A":
        Arithmatic_operations()
    elif I =="T":
        Trigonometric_calculations()
    elif I =="E":
        exponential_and_logarithmic_functions()
    else:
        print("Invalid input")

k = 0
while k < positive_infinity:
     Calculator()
     k+=1

