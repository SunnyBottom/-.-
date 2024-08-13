immutable_var = 1, 2, 3, 'apple', False
print(immutable_var)
# immutable_var[2] = 0 - выдает ошибку, тк "кортежи" неизменяемые списки
mutable_list = ['rabbit', 2, 3, 9, False]
mutable_list[0] = 'wolf'
print(mutable_list)