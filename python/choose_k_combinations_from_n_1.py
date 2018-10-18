'''
Algorithm to return all combinations of k elements from n.

write a function that takes an array of letters as an argument and a number of those letters to select.

Say you provide an array of 8 letters and want to select 3 letters from that. Then you should get:

    8! / ((8 - 3)! * 3!) = 56
Arrays (or words) in return consisting of 3 letters each.

'''


def comb(sofar, rest, n):
    if n == 0:
        print(sofar)
    else:
        for i in range(len(rest)):
            comb(sofar + rest[i], rest[i+1:], n-1)

print(comb("", "abcdefgh", 3))
