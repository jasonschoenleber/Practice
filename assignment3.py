# 1) Create a list of “person” dictionaries with a name, age and list of hobbies for each person. Fill in any data you want.
family = [
    {
        'name': 'Jason', 
        'age': 34, 
        'hobbies': ['soccer', 'reading', 'python']
    },
    {
        'name': 'Carleigh', 
        'age': 35, 
        'hobbies': ['working out', 'work']
    },
    {
        'name': 'Jayson', 
        'age': 3, 
        'hobbies': ['swimming', 'playing']
    },
    {
        'name': 'Hope', 
        'age': 1, 
        'hobbies': ['eating', 'pooping']
    }
        ]  

# 2) Use a list comprehension to convert this list of persons into a list of names (of the persons).
names = [el['name'] for el in family]
print(names)
# 3) Use a list comprehension to check whether all persons are older than 20.
ages = all([el['age'] > 20 for el in family])
print(ages)
# 4) Copy the person list such that you can safely edit the name of the first person (without changing the original list).
copy_family = [el.copy() for el in family]
check = family is copy_family
print(check)
copy_family[0]['name'] = 'Steve'
print(copy_family)
print(family)
# 5) Unpack the persons of the original list into different variables and output these variables.
a,b,c,d = family
print(a)
print(b)
print(c)
print(d)
