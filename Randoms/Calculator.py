# Calculator on CLI

import math as mathfun

Number1=0
Number2=0
Oprator=""
First_Opration=True
print("""Operators Supported: 
    +,-,/,*,^,f,b,h,e
    f => Factorial
    b => Convert to Binary
    h => Convert to Hexadecimal
    e => exponential""")

while(True):
    
    if not First_Opration:
        print(f"Previous Value is: {Number1}")
        Oprator=input("Enter C to clear, Q for quit, or Operator for next Operation: ")  
        
        if Oprator.lower() == "q":
            break

        if Oprator.lower() == "c":
            First_Opration=True
            print("memory cleared")
            continue

    elif First_Opration:
        try:
            Number1 = float(input("Enter Number: "))
        except ValueError:
            print("Invalid input")
            continue
        Oprator = input("Enter the desired Operaton: ")

    if Oprator in ["+","-","/","*","^","+"]:
        First_Opration = False
        try:
            Number2 = float(input("Enter Number: "))
        except ValueError:
            print("Invalid input")
            continue

        if Oprator == "+":
            print(f"{Number1} + {Number2} = {Number1 + Number2}")
            Number1 += Number2
            continue

        elif Oprator == "-":
            print(f"{Number1} - {Number2} = {Number1 - Number2}")
            Number1 -= Number2
            continue
        
        elif Oprator == "*":
            print(f"{Number1} x {Number2} = {Number1 * Number2}")
            Number1 *= Number2
            continue
        
        elif Oprator == "/":
            print(f"{Number1} / {Number2} = {Number1 / Number2}")
            Number1 /= Number2

        elif Oprator == "^":
            print(f"{Number1} ^ {Number2} = {Number1 ** Number2}")
            Number1 **= Number2

    if Oprator in ["f","b","h","e"]:
        First_Opration = False
        if Oprator == "b":
            Number1=(mathfun.floor(Number1))
            print(f"The binary is {bin(Number1)}")
            continue
        elif Oprator == "h":
            Number1=mathfun.floor(Number1)
            print(f"The hexadecimal is {hex(Number1)}")
            continue
        elif Oprator == "e":
            Number1 = mathfun.exp((Number1))
            print(f"The exponential is {Number1}")
            continue
        elif Oprator == "f":
            Number1 = mathfun.factorial(int(Number1))
            print(f"The factorial is {Number1}")
            continue
    else:
        print(f"Invlid operator: {Oprator} ")
