"""
Convert the input number to alphabet representation
Let 0 represent ‘A’, 1 represents ‘B’, etc. Given a digit sequence, count the number of possible decodings of the given digit 
sequence.
Input: digits[] = "121" Output: 3 ( The possible decodings are "BCB", "BV", "MB" ) Similarly "200" can be interpreted as "caa" 
or "ua" and "007" has one.

"""
def valid_two_digit_encoding(a, b):
    if not a or not b:
        return False
    if a in ('1', '2') and b < '6':
        return True
    return False

def valid_sequences(input_num):
    if len(input_num) <= 1:
        return 1

    encodings = 0
    if valid_two_digit_encoding(input_num[0], input_num[1]):
        encodings += valid_sequences(input_num[2:])

    encodings += valid_sequences(input_num[1:])

    return encodings


def countValidSequences(input_num):
    return valid_sequences(input_num)

# Input "1" output 1
print("Count ",countValidSequences("1"))
# Input "121" output 3
print("Count ",countValidSequences("121"))
# Input "200" output 2
print("Count ",countValidSequences("200"))
# Input "007" output 1
print("Count ",countValidSequences("007"))
# Input "2563" output 2
print("Count ",countValidSequences("2563"))
# Input "123" output 3
print("Count ",countValidSequences("123"))
# Input "99" output 1
print("Count ",countValidSequences("99"))
# Input "100200300" output 4
print("Count ",countValidSequences("100200300"))
# Input "2222" output 5
print("Count ",countValidSequences("2222"))
# Input "312" output 2
print("Count ",countValidSequences("312"))
