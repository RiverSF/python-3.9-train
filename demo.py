from collections.abc import Iterator
from functools import reduce
from decimal import Decimal
from io import StringIO
import json

# with open('test.txt', 'r', encoding='utf-8') as f:
#     print(f.read(10))
#
# exit()


class Chain(object):
    test = 123
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        print(path)
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__

s = Chain().z.x
print(s)
j = json.dumps(s, default=lambda obj: obj.__dict__)
print(j)
obj = json.loads(j)
print(type(obj))
exit()


def createCounter():
    _list = []
    def counter():
        last = len(_list) + 1
        _list.append(last)
        return last
    return counter
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())
exit(123)



def is_palindrome_yield(n):
    s = str(n)
    if len(s) == 1:
        yield n
    else:
        while len(s) > 1:
            if s[0] == s[-1]:
                s = s[1:-1]
                if len(s) < 2:
                    yield n
            else:
                break
for i in range(1, 100):
    palindrome = is_palindrome_yield(i)
    print(palindrome)
exit(123)

palindrome = [n for n in map(is_palindrome_yield, range(1, 100))]
print(palindrome)

def is_palindrome(n):
    s = str(n)
    if len(s) == 1:
        return True
    else:
        while len(s) > 1:
            if s[0] == s[-1]:
                s = s[1:-1]
                if len(s) < 2:
                    return True
            else:
                return False

output = filter(is_palindrome, range(1, 100))
print('1~1000:', list(output))
exit(1)



def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


def primes():
    yield 2
    it = _odd_iter()  # 初始序列
    while True:
        n = next(it)  # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it)  # 构造新序列


def _not_divisible(n):
    return lambda x: x % n > 0


# 打印1000以内的素数:
for n in primes():
    if n < 100:
        print(n)
    else:
        break
exit(1)


def fn(x, y):
    return x * y


res = reduce(fn, [1, 2, 4])
print(res)


def _map(z):
    return z + 1


_m = map(_map, [1, 2, 3])
if isinstance(_m, Iterator):
    print(list(_m))

exit(1)

_list = ['Michael', 'Bob', 'Tracy']
_tuple = (1,)
if _tuple:
    print(_tuple)

_input = input('aaa:')
print(_input)
if not isinstance(_input, (int, float)):
    raise TypeError('Bad operand type')
    print('输入参数类型不合法，%s' % _input)
else:
    print('输入参数正确，%s' % _input)

nums = list(range(100))
print(len(nums))
# for _v in nums:
#     print(_v)

# 格式化整数和浮点数还可以指定是否补0和整数与小数的位数：
print('%06d-%04d' % (3, 10))
# 000003-0010
print('%06.2f' % 3.1415926)
# 003.14


_dict = {}
_dict['a'] = 1
print(_dict.get('b'))
