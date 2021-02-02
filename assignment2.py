# Follow the instructions explained in the problem video and try to implement a solution on your own. Compare it with my solution (video + downloadable files) thereafter.
# 1) Create a list of names and use a for loop to output the length of each name (len() ).
# 2) Add an if  check inside the loop to only output names longer than 5 characters.
# 3) Add another if  check to see whether a name includes a “n”  or “N”  character.
# 4) Use a while  loop to empty the list of names (via pop() )

names = ['Jason', 'Carleigh', 'Jayson', 'Hope', 'Shadow']

for name in names:
    print(len(name))

print('Part 1')

for name in names:
    if len(name) > 5 and ('n' in name or 'N' in name):
        print(name)

print('Part 2')

while len(names) >= 1:
    print(names.pop())


