tuple = 1, 'Hello'
immutable_var = tuple
print(tuple)
#tuple[1] = 'Пока'
#Кортеж хранит лишь путь к информации, поэтому ее изменение невозможно
mutable_list = [1,2,3,4]
print(mutable_list)
mutable_list[2] = 6
print(mutable_list)