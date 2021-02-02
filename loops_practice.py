'''Exercise Question 1: Print First 10 natural numbers using while loop
Expected output:

0
1
2
3
4
5
6
7
8
9
10'''

# i = 0
# while i <= 10:
#     print(i)
#     i += 1

'''Exercise Question 2: Print the following pattern
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5'''

# newlist = []
# i = 1
# while i <= 5:
#     newlist.append(i)
#     i += 1
#     print(newlist)

'''Exercise Question 3: Accept number from user and calculate the sum of all number between 1 and given number
For example user given 10 so the output should be 55'''

# summed = 0
# number = int(input('Give me a number: '))
# for i in range(1, number + 1, 1):
#     summed += i
# print(summed)

'''Exercise Question 4: Print multiplication table of given number
For example num = 2 so the output should be

2
4
6
8
10
12
14
16
18
20'''

# number = int(input('Give me a number: '))
# i = 0
# for i in range(1, 11,1):
#     print(number * i)
#     i += 1

'''Exercise Question 5: Given a list iterate it and display numbers which are divisible by 5 and if you find number greater than 150 stop the loop iteration
list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]

Expected output:

15
55
75
150'''

# given_list = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
# n = len(given_list)
# for i in given_list:
#     if i % 5 == 0 and i < 151:
#         print(i)

'''Exercise Question 6: Given a number count the total number of digits in a number
For example, the number is 75869, so the output should be 5.'''

# number = input('Give me a number: ')
# counting = len(number)
# print(counting)

'''Exercise Question 7: Print the following pattern using for loop
5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1'''

# given_list = [5,4,3,2,1]
# i = 0
# print(given_list)
# for i in given_list:
#     given_list = given_list[1:]
#     print(given_list)

'''Exercise Question 8: Reverse the following list using for loop
list1 = [10, 20, 30, 40, 50]

Expected output:
50
40
30
20
10'''

# given_list = [10,20,30,40,50]
# for i in reversed(given_list):
#     print(i)

'''Exercise Question 9: Display -10 to -1 using for loop

Expected output:

-10
-9
-8
-7
-6
-5
-4
-3
-2
-1'''

# for i in reversed(range(1, 11)):
#     print(i * -1)


'''Exercise Question 10: Display a message “Done” after successful execution of for loop
For example, the following loop will execute without any error.

for i in range(5):
    print(i)
So the Expected output should be:

0
1
2
3
4
Done!'''

# for i in range(5):
#     print(i)
# print('Done!')
