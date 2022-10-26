import math





_tuple = (1,2,3,4,5)
print(type(_tuple))
print(_tuple[0])
print(_tuple[1])
print(_tuple[2])
print(type(_tuple[1]))
print('x = %d' % _tuple[0])

exit()



_str = 'AVc'
_str.capitalize()
_str = _str.strip('c')
print(_str)
exit(1)

_list = [1, 2, 3, 5, 6, 78, 11]
print(_list[1: -1])
_str = ''
print(_str[1:-1])

min = min(_list)
max = max(_list)
print(min, max)

def findminmax(L):
    _min = L[0]
    print(_min)
    _max = L[0]
    for val in L:
        if val < _min:
            _min = val
        elif val > _max:
            _max = val
    return (_min, _max)
print(findminmax(_list))

for list_val in _list:
    print(list_val)
for list_key, list_val in enumerate(_list):
    print(list_key, list_val)
for tuple_val_1, tuple_val_2 in [(1, 2), (3, 4)]:
    print(tuple_val_1, tuple_val_2)
for list_val_1, list_val_2 in [[5, 6], [3, 4]]:
    print(list_val_1, list_val_2)
for dict_key in {'a': 'b'}:
    print(dict_key)
for dict_val in {'a': 'b'}.values():
    print(dict_val)
for dict_key, dict_val in {'a': 'b'}.items():
    print(dict_key, dict_val)


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


x, y = move(1, 2, 3)
print(x, y)
