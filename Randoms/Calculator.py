# Calculator on CLI

import math as mathfun

Numebr1=0
Number2=0
Oprator=""
First_Opration=True
print("""Operators Supported: 
    +,-,/,*,^,b,h,e""")

while(True):
    
    if not First_Opration:
        print(f"Previous Value is: {Numebr1}")
        Oprator=input("Enter C to clear, Q for quit, or Operator for next Operation: ")  
        
        if Oprator.lower() == "q":
            break

        if Oprator.lower() == "c":
            First_Opration=True
            print("memory cleared")
            continue

    elif First_Opration:
        try:
            Numebr1 = float(input("Enter Number: "))
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
            print(f"{Numebr1} + {Number2} = {Numebr1 + Number2}")
            Numebr1 += Number2
            continue

        elif Oprator == "-":
            print(f"{Numebr1} - {Number2} = {Numebr1 - Number2}")
            Numebr1 -= Number2
            continue
        
        elif Oprator == "*":
            print(f"{Numebr1} x {Number2} = {Numebr1 * Number2}")
            Numebr1 *= Number2
            continue
        
        elif Oprator == "/":
            print(f"{Numebr1} / {Number2} = {Numebr1 / Number2}")
            Numebr1 /= Number2

        elif Oprator == "^":
            print(f"{Numebr1} ^ {Number2} = {Numebr1 ** Number2}")
            Numebr1 **= Number2

    if Oprator in ["b","h","e"]:
        First_Opration = False
        if Oprator == "b":
            Number1=(mathfun.floor(Numebr1))
            print(f"The binary is {bin(Number1)}")
            continue
        elif Oprator == "h":
            Numebr1=mathfun.floor(Numebr1)
            print(f"The hexadecimal is {hex(Numebr1)}")
            continue
        elif Oprator == "e":
            Number1 = mathfun.exp((Numebr1))
            print(f"The exponential is {Numebr1}")
            continue
    
    else:
        print(f"Invlid operator: {Oprator} ")