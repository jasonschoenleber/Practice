name = input('Please Type Your Name: ')
age = int(input('Please Type Your Age: '))


def get_info():
    print(name + str(age))


def calc_decades():
    print(age // 10)


get_info()
calc_decades()