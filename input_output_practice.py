'''Exercise Question 1: Accept two numbers from the user and calculate multiplication'''

# def multiplication():
#     first_number = int(input('What is the first number?: '))
#     second_number = int(input('What is the second number?: '))
#     print(first_number * second_number)

# multiplication()

'''Exercise Question 2: Display “My Name Is James” as “My**Name**Is**James” using output formatting of a print() function'''

# star = '**'
# print(f'My{star}Name{star}Is{star}James')

'''Exercise Question 3: Convert decimal number to octal using print() output formatting
Expected Output:
Display decimal number 8 as 10'''

# def convert():
#     number = int(input('what number will you convert?: '))
#     value = oct(number)
#     print(value)

# convert()

'''Exercise Question 4: Display float number with 2 decimal places using print()
Expected Output:
Display 458.541315 as 458.54'''

# def float_convert():
#     number = float(input('Enter any float: '))
#     print(round(number,2))

# float_convert()

'''Exercise Question 5: Accept list of 5 float numbers as a input from user'''

# newlist = []

# n = int(input('Enter the list of numbers: '))

# for i in range(0, n):
#     ele = int(input('Enter a number: '))
    
#     newlist.append(ele)
#     print(newlist)

'''Exercise Question 7: Accept any three string from one input() call'''

# str1, str2, str3 = input('Enter 3 strings: ').split()
# print(str1, str2, str3)
# print(str1, str2)
# print(str1)

'''Exercise Question 8: You have the following data.
totalMoney = 1000
quantity = 3
price = 450
display above data using string.format() method
I have 1000 dollars so I can buy 3 football for 450.00 dollars.'''

totalMoney = 1000
quantity = 3
price = 450
print(f'I have {totalMoney} dollars so I can buy {quantity} fotball(s) for {price} dollars.')
