def pyr(n):
    num = 1

    for i in range(1,n+1):
        #num = 1
        for n in range(1,i+1):
            print(num, end= " ")
            num = num + 1
        print("\r")

pyr(10)
