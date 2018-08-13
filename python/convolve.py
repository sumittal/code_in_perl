def convolve(a, k):
    
    len_a = len(a)
    len_k = len(k)
    tmp = []
    
    for sublist in chunks(a, len_k):
        #print('aa ', sublist)
        sums = 0 
        for j in range(len_k):
            if len(sublist) == len_k:
                sums += sublist[j] * k[j]
            else:
                return tmp
            
        tmp.append(sums)
        
            
def chunks(l, n):
    for i in range(0, len(l)):
        yield l[i:i + n]

a=[1,2,3,4,5,6,7,8,9,10]
k=[1,2,1]

print(convolve(a,k))
