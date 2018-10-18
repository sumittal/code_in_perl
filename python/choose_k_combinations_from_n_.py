'''
Algorithm to return all combinations of k elements from n.

write a function that takes an array of letters as an argument and a number of those letters to select.

Say you provide an array of 8 letters and want to select 3 letters from that. Then you should get:

    8! / ((8 - 3)! * 3!) = 56
Arrays (or words) in return consisting of 3 letters each.

'''

def choose_iter(elements, length):
    for i in range(len(elements)):
        if length == 1:
            yield (elements[i],)
        else:
            for next in choose_iter(elements[i+1:len(elements)], length-1):
                yield (elements[i],) + next

print("total combinations : ", len(list(choose_iter("abcdefgh",3))))
for w in choose_iter("abcdefgh",3):
    print(w, end="\n")

#def choose(l, k):
#    return list(choose_iter(l, k))
