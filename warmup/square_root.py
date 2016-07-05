def square_root(n):

    is_neagtive = False

    if( n < 0 ):
        n = -n
        is_neagtive = True

    start = 0
    end = n
    mid = float(start + end)/2
    prev_mid = 0
    diff = abs(mid - prev_mid)
    precision = 0.0005

    while( (mid * mid != n) and (diff > precision) ):
        if(mid * mid > n):
            end = mid
        else:
            start = mid

        prev_mid = mid
        mid = float(start + end)/2
        diff = abs(mid - prev_mid)

    return str(mid) + ('i' if is_neagtive else '')

number = int(raw_input('Enter the number to calculate the square root : '))
print "Square root of " + str(number) + " = " + square_root(number)

'''
Steps:
Use binary search to find the square root.
1. Initialize, start = 0, end = number, mid = (start+end)/2.
2. Set prevMid = 0, as the previous mid value.
3. Find diff = absolute difference between prevMid and mid.
4. While mid is not the square root of number (i.e. mid*mid != number) and difference diff is greater than 0.0005, 
repeat the following steps:
   a. If mid*mid > number, then the square root will be less than mid. So, set end = mid.
   b. Else, the square root will be greater than mid. So, set start = mid.
   c. Set prevMid = mid
   d. Re-evaluate mid  = (start+end)/2.
   e. Re-evaluate diff from prevMid and mid.
'''
