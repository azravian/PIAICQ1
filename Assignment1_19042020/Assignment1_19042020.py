'''
Assignment 1: print sum, subtraction, divison, and multiplication of two numbers input by User 
Assigned by Sir Inam
Assignment date: 19-04-2020
'''
#input of 2 numbers

Number1=int(input("Enter First Number: "))
Number2=int(input("Enter Second Number: "))

#addintion of two numbers
sum_result = Number1 + Number2
print(f"sum is of {Number1} and {Number2} is {sum_result}")
del sum_result   #del variable, not required for this code, but a good practice to do so


#subtraction of two numbers
sub_result = Number1 - Number2
print(f"The result of {Number1} - {Number2} is {sub_result}")
del sub_result   #del variable 

#Division of two numbers
div_result = Number1 / Number2
mod_result = Number1 % Number2 
print(f"The result of {Number1} divided by {Number2} is {div_result}")
del div_result   #del variable 

#Multiplication of two numbers
mult_result = Number1 * Number2
print(f"The result of {Number1} multiplied by {Number2} is {mult_result}")
del mult_result   #del variable 


'''
#Mod of two numbers
mod_result = Number1 % Number2
print(f"The mod of {Number1} and {Number2} is {mod_result}")
del mod_result   #del variable 

#Number1 raised to power Number
pow_result = Number1 ** Number2
print(f"The result of {Number1} raised to power {Number2} is {pow_result}")
del pow_result   #del variable 

'''