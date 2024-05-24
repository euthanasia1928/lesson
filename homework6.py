my_dict = {'Sasha': 112, 'Lexa': 117}
print(my_dict.get('Sasha'))
print(my_dict.get('Nekit'))
my_dict['Egor']= 192
my_dict['Nastya'] = 923
my_dict['Egor']= 192
my_dict['Nastya'] = 923
print(my_dict)
c = my_dict.pop('Sasha')
print(c)
print(my_dict)

my_set = {1,2,3,1,2,'Hello','Hi','Hello'}
print(my_set)
my_set.add(7)
my_set.add(9)
print(my_set)
my_set.remove(2)
print(my_set)