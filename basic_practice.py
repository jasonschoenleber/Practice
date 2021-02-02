# Coding Exercises
'''Write a function that returns the maximum of two numbers.'''

# def maxnumber():
#     first_number = input('Give me the first number: ')
#     second_number = input('Give me the second number: ')
#     if first_number > second_number:
#         print(first_number)
#     else:
#         print(second_number)

# maxnumber()

'''Write a function called fizz_buzz that takes a number.
If the number is divisible by 3, it should return “Fizz”.
If it is divisible by 5, it should return “Buzz”.
If it is divisible by both 3 and 5, it should return “FizzBuzz”.
Otherwise, it should return the same number.'''

# def fizz_buzz():
#     number = input('Give me a number: ')
#     if int(number) % 5 == 0 and int(number) % 3 == 0:
#         print('FizzBuzz')
#     elif int(number) % 3 == 0:
#         print('Fizz')
#     elif int(number) % 5 == 0:
#         print('Buzz')

# fizz_buzz()

'''Write a function for checking the speed of drivers. This function should have one parameter: speed.
If speed is less than 70, it should print “Ok”.
Otherwise, for every 5km above the speed limit (70), it should give the driver one demerit point and print the total number of demerit points. 
For example, if the speed is 80, it should print: “Points: 2”.
If the driver gets more than 12 points, the function should print: “License suspended”'''

# def speed_check():
#     speed = input('What is the drivers speed?: ')
#     if int(speed) < 70:
#         print("Ok")
#     elif int(speed) == 70:
#         print(1)
#     elif int(speed) > 70 and (1 + ((int(speed) - 70)//5) > 12):
#         print('License Suspended')
#     elif int(speed) > 70:
#         print(1 + ((int(speed) - 70)//5))

# speed_check()

'''Write a function called showNumbers that takes a parameter called limit. 
It should print all the numbers between 0 and limit with a label to identify the even and odd numbers. 
For example, if the limit is 3, it should print:
0 EVEN
1 ODD
2 EVEN
3 ODD'''

# def showNumbers():
#     limit = input('What is the limit?: ')
#     i = 0
#     while i <= int(limit):
#         if i % 2 == 0:
#             a = 'EVEN'
#         else:
#             a = 'ODD'
#         print(str(i) + ' ' +a)
#         i += 1

# showNumbers()

'''Write a function that returns the sum of multiples of 3 and 5 between 0 and limit (parameter). 
For example, if limit is 20, it should return the sum of 3, 5, 6, 9, 10, 12, 15, 18, 20.'''

def multiples():
    limit = input('What is the limit?: ')




'''Write a function called show_stars(rows). If rows is 5, it should print the following:
*
**
***
****
*****'''

# def show_stars():
#     rows = input('How many rows?: ')
#     i = 0
#     while i <= int(rows):
#         print('*' * i)
#         i += 1

# show_stars()

'''Write a function that prints all the prime numbers between 0 and limit where limit is a parameter'''

# def print_prime():
#     limit = input('What is the limit?: ')
#     i = 0
#     while i <= int(limit):
#         if i 

'''Question 1: Given a two integer numbers return their product and  if the product is greater than 1000, then return their sum'''

# def inputs():
#     number1 = int(input('What is the first number?: '))
#     number2 = int(input('What is the second number?: '))
#     Sum = number1 + number2
#     Product = number1 * number2
#     if number1 * number2 > 1000:
#         print('Sum = ' + str(Sum) + ' Product = ' + str(Product))
#     else:
#         print('Product = ' + str(Product))

# inputs()

'''Question 2: Given a range of first 10 numbers, Iterate from start number to the end number and print the sum of the current number 
and previous number'''

# def range_print(num):
#     previousnum = 0
#     for i in range(num):
#         Sum = previousnum + i
#         print('Current Number: ', i, ' Previous Number: ', previousnum, ' Sum: ', Sum)
#         previousnum = i

# range_print(10)

'''Question 3: Given a string, display only those characters which are present at an even index number.
For example str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’.'''

# def even_letters():
#     word = input('Please type a word: ')
#     for i in range(0, len(word)-1, 2):
#         print(word[i])

# even_letters()

'''Question 4: Given a string and an integer number n, remove characters from a string starting from zero up to n and return a new string
For example, removeChars("pynative", 4) so output must be tive. Note: n must be less than the length of the string.'''

# def word_update():
#     word = input('Type a word to update: ')
#     length = len(word)
#     number = int(input('How many letters do you want to remove?: '))
#     print(word[number:length])

# word_update()
        
'''Question 5: Given a list of numbers, return True if first and last number of a list is same'''

# numlist = [10, 20, 30, 40, 10]

# def list_check():
#     if (numlist[0] == numlist[-1]):
#         print(True)
#     else:
#         print(False)

# list_check()

'''Question 6: Given a list of numbers, Iterate it and print only those numbers which are divisible of 5'''

# Given_List = [23,45,56,60,76,85,90,101]

# def multiple_of_five():
#     for i in Given_List:
#         if (i % 5 == 0):
#             print(i)

# multiple_of_five()

'''Question 7: Return the total count of sub-string “Emma” appears in the given string
Given string is “Emma is good developer. Emma is a writer”'''

# def substringcount():
#     string = 'Emma is good developer. Emma is a writer'
#     print(string.count('Emma'))
    

# substringcount()

'''Question 8: Print the following pattern
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5'''

# def printer():
#     for i in range(6):
#         print(str(i)*i)
#         i += 1

# printer()

'''Question 9: Reverse a given number and return true if it is the same as the original number'''

# def reverse_check():
#     number = input('What is the number we are checking?: ')
#     reversed = str(number)[::-1]
#     if reversed == number:
#         print(reversed)
#         print(True)
#     else:
#         print(reversed)
#         print(False)

# reverse_check()

'''Question 10: Given a two list of numbers create a new list such that new list should contain only odd numbers from the first list and 
even numbers from the second list
First List  [10, 20, 23, 11, 17]
Second List  [13, 43, 24, 36, 12]
result List is [23, 11, 17, 24, 36, 12]'''

# First_List = [10, 20, 23, 11, 17]
# Second_List = [13, 43, 24, 36, 12]
# combined_list = []

# def combined():
#     for i in First_List:
#         if (i % 2 != 0):
#             combined_list.append(i)
#     for i in Second_List:
#         if (i % 2 == 0):
#             combined_list.append(i)
#     print(combined_list)

# combined()

'''Question 11: Write a code to extract each digit from an integer, in the reverse order'''

# def reverse():
#     number = int(input('What number do you want to flip?: '))
#     print(int(str(number)[::-1]))

# reverse()

'''Question 12: Calculate income tax for the given income by adhering to the below rules
Taxable Income	 Rate (%)
First $10,000	 0
Next $10,000	 10
The remaining	 20'''

# def taxes():
#     income = int(input('What is your income?: '))
#     if income <= 10000:
#         print('0')
#     elif income <=20000:
#         print((income-10000)*.1)
#     elif income > 20000:
#         print(((income-20000)*.2)+1000)

# taxes()

'''Question 13: Print multiplication table form 1 to 10
Expected Output:
1  2 3 4 5 6 7 8 9 10 		
2  4 6 8 10 12 14 16 18 20 		
3  6 9 12 15 18 21 24 27 30 		
4  8 12 16 20 24 28 32 36 40 		
5  10 15 20 25 30 35 40 45 50 		
6  12 18 24 30 36 42 48 54 60 		
7  14 21 28 35 42 49 56 63 70 		
8  16 24 32 40 48 56 64 72 80 		
9  18 27 36 45 54 63 72 81 90 		
10 20 30 40 50 60 70 80 90 100 '''

# def multiplication():
#     for i in range(1,11):
#         print(i, i*2, i*3, i*4, i*5, i*6, i*7, i*8, i*9, i*10)
        
# multiplication()

'''Question 14: Print downward Half-Pyramid Pattern with Star (asterisk)
* * * * *  
* * * *  
* * *  
* *  
*'''

# def starprint():
#     for i in range(5):
#         print('*' * (5-i))
#         i += 1

# starprint()

'''Question 15: Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.
Note here exp is a non-negative integer, and the base is an integer.
Expected Output:
Case 1:
base = 2
exponent = 5
2 raises to the power of 5 is: 32 i.e. (2 *2 * 2 *2 *2 = 32)

Case 2:
base = 5
exponent = 4
5 raises to the power of 4 is: 625 i.e. (5 *5 * 5 *5 = 625)'''

# base = int(input('What is the base?: '))
# exp = int(input('What is the exponent?: '))

# def exponent(base, exp):
#     print(base**exp)
    
# exponent(base, exp)