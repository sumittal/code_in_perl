"""
Segregate Even and Odd numbers
Input  = {12, 34, 45, 9, 8, 90, 3}
Output = {12, 34, 8, 90, 45, 9, 3} 
"""

def segregateEvenOdd(arr):
    
    l, r = 0, len(arr) - 1
    
    while l < r:
        
        # Increment left index while we see 0 at left
        while (arr[l]%2 == 0 and l < r):
            l += 1
            
        while(arr[r]%2 == 1 and l < r):
            r -= 1
            
        if(l < r):
            # swap arr[l] and arr[r]
            arr[l],arr[r] = arr[r],arr[l]
            
            l += 1
            r -= 1
            
# Driver function to test above function
arr = [12, 34, 45, 9, 8, 90, 3]
segregateEvenOdd(arr)
print("Array after segregation "),
for i in range(0,len(arr)):
    print(arr[i])
