'''
Write function that should return true if the target integer can be obtained by placing addition or subtraction operations in the list.

Example :

f(5, [5, 2]) = false. There's no way to add or subtract 5 and 2 to get 5.

f(13, [3, 9, 3, 2]) = true. 3 + 9 + 3 - 2 = 13.

f(0, []) = true

f(1, []) = false
'''

def getWays(magic_number, numbers):
    if (util(numbers, 0, magic_number) > 0):
        return True
    return False


def util(numbers, i, magic_number):
    n = len(numbers)

    if i == n and magic_number != 0:
        return 0

    if magic_number == 0 and i == n:
        return 1

    return 1 if 1 in (util(numbers, i + 1, magic_number - numbers[i]), util(numbers, i + 1, magic_number + numbers[i])) else 0


if (getWays(13, [3, 9, 3, 2])):
    print("True")
else:
    print("False")

if (getWays(5, [5, 2])):
    print("True")
else:
    print("False")
