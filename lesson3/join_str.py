def func(*kvargs, glue=':'):
    final_str = []
    for str in kvargs:
        if len(str) > 3:
            final_str.append(str)
    return glue.join(final_str)

print(func('test', 'qw', 'tnt', 'A', 'Popopo'))