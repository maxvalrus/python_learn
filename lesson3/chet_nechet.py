def test(my_list, my_bool):
    nechet = []
    chet = []

    for i in my_list:
        if i % 2 == 0:
            nechet.append(i)
        else:
            chet.append(i)

    if my_bool:
        return nechet
    else:
        return chet

my_list = [4,3,5,7,8]

print(test(my_list, False))