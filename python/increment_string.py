# Write a function which increments a string, to create a new string. 
# If the string already ends with a number, the number should be incremented by 1. 
# If the string does not end with a number, the number 1 should be appended to the new string.
#     Examples:
#     foo -> foo1
#     foobar23 -> foobar24
#     foo23bar -> foo23bar1
#     foo0042 -> foo0043
#     foo9 -> foo10
#     foo1000 -> foo1001
#     foo099 -> foo100
#     Attention: If the number has leading zeros the number of digits should be considered.

import re
def incrementString(s):
    res = re.search(r'\d+$', s)
    if res:
        number = int(res.group())
    else:
        return None

    new_number = number + 1

    return s.replace(str(number), str(new_number))

print(incrementString('foo099'))
print(incrementString('foo0042'))
