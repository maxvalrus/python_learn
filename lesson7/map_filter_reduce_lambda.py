from functools import reduce

l = [1, 4, 5, 30, 99]
s = map(lambda x: x % 5, l)
print(list(s))

ls = [3, 4, 90, -2]
ss = map(lambda x: str(x), ls)
print(list(ss))

fl = ['some', 1, 'v', 40, '3a', str]
fs = filter(lambda x: not isinstance(x, str), fl)
print(list(fs))

rl = ['some', 'other', 'value']
rs = reduce(lambda a, b: a + b, list(len(x) for x in rl))
print(rs)