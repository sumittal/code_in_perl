#!/bin/python

import sys
import os


# CalculateArraySizeTest
# The idea behind the test is to find the size of an array.
# The Array is virtual and is not implemented as a traditional memory array. 
# Actual implementation is hidden, but the array elements may be accessed by
# the methods provided by this class.
#

#Max size of the virtual array (1 million)
MAX_ARRAY_SIZE = 1000000 ;

ACTUAL_ARRAY_SIZE = 1000
op = 0
def test(array_size):
    global op, ACTUAL_ARRAY_SIZE
    op = 0
    ACTUAL_ARRAY_SIZE = array_size
    
    sz = findArraySize()
    
    print "Array size="+str(sz)+ ". Total calls made="+str(op)
    return sz 
    
    
def getElement(index):
    """
     * This method provides access to the elements of the virtual array. 
     * Array size could vary between 0 and 1 million.
     * Index must be 1 based. Contents of array at the specified index are returned as return value
     * of this method if the index is legal. If the specified index is not legal, then 
     * ValueError exception is thrown.
     *
     * Accessing of the virtual array could be a costly operation and hence calls to this method
     * should be minimized.
     *
     * @param       index    Index into the virtual array
     * @return      Contents of virtual array at the index specified by lIndex parameter, if the index
     *              is within bounds of the virtual array.
     * @raises      ValueError if the index parameter is out of bounds.
     *
     """  
    global op
    op = op +1
    if (index <= 0) or (index >  ACTUAL_ARRAY_SIZE):
        raise ValueError("Index out of bounds")
    return 100


# Complete the function below.

def findArraySize():
    """
    Using the getElement() as the only function to invoke, find the virtual array size
    The only constraint is to minimize the number of calls to getElement()
    
    Your code will be checked for understanding of problem, logic, memory usage etc    
    
    """
    
    array_size = 0
    
    #Your code here
    l = 0
    r = MAX_ARRAY_SIZE
    flag = True
    while r >= l:
        try:
            mid = (l + r-1)/2
            if l == r:
                flag = False
            getElement(mid)
            l = mid + 1
            
        except:
            r = mid -1
    if flag:        
        array_size = r
    else:
        array_size=mid
    return array_size


_array_size = int(raw_input())

res = test(_array_size)
print res