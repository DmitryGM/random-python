#!/usr/bin/python


def num_of_items(count):
    if count > 10:
        count = 'many'
    return f'Number of: {count}'


def start_end_symbols(s):
    """
    'welcome' -> 'weme'
    """
    return s[:2] + s[-2:]


print(start_end_symbols('welcome'))


# Example: 'bibble' -> 'bi**le'
# s.replace(stra, strb)
def replace_char(s):
    return s[0] + s[1:].replace(s[0], '*')


print(replace_char('bibble'))


# Example:
# 'max', pid' -> 'pix mad'
# 'dog', 'dinner' -> 'dig donner'
def str_mix(a, b):
    return ' '.join([b[:2] + a[2:], a[:2] + b[2:]])


print(str_mix('max', 'pid'))
print(str_mix('dog', 'dinner'))


# Provided simple test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(res, expt):
    pass


# test(start_end_symbols('welcome'), 'weme')
#
# test(replace_char('bibble'), 'bi**le')



if __name__ == '__main__':
    pass
    #main()
