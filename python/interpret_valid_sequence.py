def countValidSequences(input_num):

    n = len(input_num)
    number = list(input_num)

    occurance = [0] * (n+1) 
    occurance[0] = 1
    occurance[1] = 1
 
    for i in range(2, n+1):
     
        occurance[i] = 0
 
        if (number[i-1] > '0'):
            occurance[i] += occurance[i-1]
 
        #if (number[i-2] == '1' or (number[i-2] == '2' and number[i-1] < '6') ):
        if (number[i-2] < '2' or (number[i-2] <= '2' and number[i-1] < '6') ):
            occurance[i] += occurance[i-2]

    return occurance[n]
 
 
 
print("Count ",countValidSequences("200"))
print("Count ",countValidSequences("2563"))
print("Count ",countValidSequences("123"))
print("Count ",countValidSequences("99"))
print("Count ",countValidSequences("100200300"))
