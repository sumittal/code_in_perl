#Class queue for use later
class Queue:
    def __init__(self):
        self.lst = []
 
    def is_empty(self):
        return self.lst == []
 
    def enqueue(self, elem):
        self.lst.append(elem)
 
    def dequeue(self):
        return self.lst.pop(0)
 
# Prints all jumping numbers smaller than or equal to
# x starting with 'num'. It mainly does BFS starting
# from 'num'.
def bfs(x,num):
 
    # Create a queue and enqueue i to it
    q = Queue()
    q.enqueue(num)
 
    # Do BFS starting from 1
    while (not q.is_empty()):
        num = q.dequeue()
 
        if num<=x:
            print(str(num),end=' ')
            last_dig = num % 10
 
            # If last digit is 0, append next digit only
            if last_dig == 0:
                q.enqueue((num * 10) + (last_dig + 1))
 
            # If last digit is 9, append previous digit
            # only
            elif last_dig == 9:
                q.enqueue((num * 10) + (last_dig - 1))
 
            # If last digit is neighter 0 nor 9, append
            # both previous digit and next digit
            else:
                q.enqueue((num * 10) + (last_dig - 1))
                q.enqueue((num * 10) + (last_dig + 1))
 
# Prints all jumping numbers smaller than or equal to
# a positive number x
def printJumping(x):
    print (str(0), end=' ')
    for i in range(1,10):
        bfs(x, i)
 
# Driver Program ( Change value of x as desired )
x = 40
printJumping(x)

"""
Print all Jumping Numbers smaller than or equal to a given value
A number is called as a Jumping Number if all adjacent digits in it differ by 1. The difference between ‘9’ and ‘0’ is not considered as 1.
All single digit numbers are considered as Jumping Numbers. For example 7, 8987 and 4343456 are Jumping numbers but 796 and 89098 are not.

Given a positive number x, print all Jumping Numbers smaller than or equal to x. The numbers can be printed in any order.
https://www.geeksforgeeks.org/print-all-jumping-numbers-smaller-than-or-equal-to-a-given-value/

"""
