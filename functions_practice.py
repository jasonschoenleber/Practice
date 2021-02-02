'''Exercise Question 1: Create a function that can accept two arguments name and age and print its value'''

# def name_age():
#     name = input('What Is Your Name?: ')
#     age = input('What Is Your Age?: ')
#     print(f'My name is {name} and I am {age} years old')

# name_age()

'''Exercise Question 2: Write a function func1() such that it can accept a variable length of  argument and print all arguments value
func1(20, 40, 60)
func1(80, 100)
Expected Output:
After func1(20, 40, 60):
20
40
60
After func1(80, 100):
80
100'''

# def func1(a, b, c):
#     print(a)
#     print(b)
#     print(c)

# func1(20, 40, 60)

'''Exercise Question 3: Write a function calculation() such that it can accept two variables and calculate the addition and subtraction of it. 
And also it must return both addition and subtraction in a single return call
For example:
def calculation(a, b):
    # Your Code
res = calculation(40, 10)
print(res)
A res should produce result 50, 30'''

# def calculation(a, b):
#     return a - b, a + b


# res = calculation(40, 10)
# print(res)

'''Exercise Question 4: Create a function showEmployee() in such a way that it should accept employee name, and it’s salary and display both, 
and if the salary is missing in function call it should show it as 9000
Expected Output:
showEmployee("Ben", 9000)
showEmployee("Ben")
Should Produce:
Employee Ben salary is: 9000
Employee Ben salary is: 9000'''

# def showEmployee(name, salary=9000):
#         print('Employee', name, 'salary is:', salary)

# showEmployee('ben', 898)

'''Exercise Question 5: Create an inner function to calculate the addition in the following way
Create an outer function that will accept two parameters a and b
Create an inner function inside an outer function that will calculate the addition of a and b
At last, an outer function will add 5 into addition and return it'''

# def outer(a, b):
#     def add():
#         return a + b
#     print(add() + 5)

# outer(1,5)

'''Exercise Question 6: Write a recursive function to calculate the sum of numbers from 0 to 10
Expected Output:
55'''

# def recursive():
#     summed = 0
#     for i in range(1, 11):
#         summed = summed + i
#     print(summed)

# recursive()

'''Exercise Question 8: Generate a Python list of all the even numbers between 4 to 30
Expected Output:
[4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]'''

# newlist = []
# for i in range(4,30,2):
#     newlist.append(i)
# print(newlist)

'''Exercise Question 9: Return the largest item from the given list
aList = [4, 6, 8, 24, 12, 2]
Expected Output:
24'''

# aList = [4,6,8,24,12,2]

# def maxlist():
#     print(max(aList))

# maxlist()