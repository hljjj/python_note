from copy import copy

a = 10000
b = 10000
copy_a = copy(a)
eq_a = a

if eq_a is a:
    print("eq_a is a")
else:
    print('eq_a is not a')

if b is a:
    print("b is a")
else:
    print("b is not a")

