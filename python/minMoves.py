def minMoves(avg):
    countof1 = 0
    size = len(avg)  

    for i in range(size):
        if (avg[i] == 1):
            countof1 += 1
  
    length = countof1
  
    max1s = -2147483648
  
    numarray={}
  
    if (avg[0] == 1):
        numarray[0] = 1
    for i in range(1,size):
        if (avg[i] == 1):
            numarray[i] = numarray[i - 1] + 1
        else:
            numarray[i] = numarray[i - 1]
   
  
    for i in range(length-1,size):
        if (i == (length - 1)): 
            countof1 = numarray[i]
        else:
            countof1 = numarray[i] - numarray[i - length]
      
        if (max1s < countof1):
            max1s = countof1
   
  
    noOfZeroes = length - max1s
  
    return noOfZeroes

