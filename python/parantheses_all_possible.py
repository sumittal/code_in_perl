#Implement an algorithm to print all valid (e.g. properly opened and closed) 
# combinations of n pair of parentheses.
"""
def compute_all_parens (n, left, right, s):
    if right == n:
        print (s)
        return
    if left < n:
        compute_all_parens(n, left+1, right, s + "(")
    if right < left:
        compute_all_parens(n, left, right+1, s + ")")



print(compute_all_parens(5, 0, 0, ""))
"""

def print_all_parens(n):
    def print_parens(left, right, s):
        if right == n:
            print(s)
            return
        if left < n:
            print_parens(left + 1, right, s + "(")
        if right < left:
            print_parens(left, right + 1, s + ")")

    return print_parens(0, 0, "")

print(print_all_parens(3))

