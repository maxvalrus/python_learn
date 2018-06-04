def deco(func):
    def test_deco(text):
        print('Decoration: ')
        func(text)
    return test_deco

@deco
def pr_str(text):
    print('My text is ', text)

pr_str('la la la')

