# 列表生成式
from collections.abc import Iterator

def _gen():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'
c = _gen()
print(c.send(None))
print(c.send(2))

exit()

def triangles():
    L = [1]
    n = 10
    while n:
        yield L
        # 第n行去掉收尾1的中间部分的每个元素等于第n-1相邻两元素相加之和
        L = [L[i - 1] + L[i] for i in range(1, len(L))]
        L.insert(0, 1)  # 头上添1
        L.append(1)  # 尾巴添1
        n -= 1


""" 判断是否是迭代器 """
""" 可以进行 for 循环的，一定是 Iterable 类型，可以通过 next() 方法返回数据的一定是 Iteration 类型 """
""" 可迭代对象不一定是迭代器：可使用 iter 方法将 Iterable 转换成 Iterator 对象"""
print(isinstance(iter([]), Iterator))
print(isinstance(iter({}), Iterator))
print(isinstance(iter(()), Iterator))
print(isinstance(triangles(), Iterator))

for i in triangles():
    print(i)
