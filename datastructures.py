simple_list = [1,2,3,4]
simple_list.extend([5,6,7])
del(simple_list[0])
print(simple_list)

d = {'name': 'Jason'}
print(d.items())
for k, v in d.items():
    print(k, v)

t = (1,2,3)
print(t.index(1))

s = {'Jason', 'Anna', 'Jason'}
print(s)


def unlimited_arguments(*args, **keyword_args):
    print(keyword_args)
    for k, argument in keyword_args.items():
        print(k, argument)


unlimited_arguments(1,2,3,4, name='Jason', age=34)