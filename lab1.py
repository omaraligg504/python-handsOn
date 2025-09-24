# Lab:
# 	- write a program that prints hello world
# print("hello world")
# 	- application to take a number in binary form from the user, and print it as a decimal

# while True:
#     binary_str = input().strip()
#     if binary_str.count('1') + binary_str.count('0') != len(binary_str):
#         print("enter valid binary number")
#
#     else:
#         decimal_str = int(binary_str, 2)
#         print(decimal_str)
#         break

# print(decimal_str)

# 	- write a function that takes a number as an argument and if the number
# 		divisible by 3 return "Fizz" and if it is divisible by 5 return "buzz" and if is is
# 		divisible by both return "FizzBuzz"
# def take(num):
# 	if isinstance(type(num),int):
# 		if not num%3 and not num%5:
# 			return "FizzBuzz"
# 		if not num%3:
# 			return "Fizz"
# 		if not num%5:
# 			return "Buzz"
# 	else:
# 		return "neither visible by 3 nor 5"
# print( take(":r"))

# 	- Ask the user to enter the radius of a circle print its calculated area and circumference

# while True:
#     try:
#         num = float(input())
#         area = 3.14 * num ** 2
#         circumference = 2 * 3.14 * num
#         print(f"Area is {area}")
#         print(f"Circumference is {circumference}")
#         break
#     except ValueError:
#         print("Enter a valid number")
# 	- Ask the user for his name then confirm that he has entered his name (not an empty string/integers). then proceed to ask him for his email and print all this data
# while True:
#     name = input()
#
#     if not name.strip() or not name.isalpha():
#         print("enter valid name")
#     else:
#         email = input()
#         if not email.strip() or not '@' in email or not '.' in email or email.find('@') or email.find('.') or email.find('@')>email.find('.'):
#             print("enter valid email ")
#         else:
#             print("Your name is " + name + " Your email is " + email)
#             break
# 	- Write a program that prints the number of times the substring 'iti' occurs in a string
# print("itiitiitiitiitiitiiti".count('iti'))
