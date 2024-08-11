def print_params(a=1, b='строка', c=True):
    print(a, b, c)


values_list = ['Vera', False, 2.48]
values_dict = {'a': True, 'b': 99, 'c': 'Hi'}


print_params(4, 1,9)
print_params(1, 25, [1, 2, 3])
print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['autumn', 67]
print_params(*values_list_2, 42)
