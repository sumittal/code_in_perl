"""
Algorithm to find the total number of connected sets in a matrix

"""
def findNumberConnected(a,b,z):
    
    canUp = (a - 1 >= 0);
    canDown = (a + 1 < len(z));
    canRight = (b + 1 < len(z[0]));
    canLeft = (b - 1 >= 0);
    
    value = 1;
    
    up = 0;
    down = 0;
    right = 0;
    left = 0;
    
    z[a][b] = 2;
    
    if canUp and z[a-1][b] == value:
        up = findNumberConnected(a-1,b,z)
    if canDown and z[a+1][b] == value:
        down = findNumberConnected(a+1,b,z)
    if canLeft and z[a][b-1] == value:
        left = findNumberConnected(a,b-1,z)
    if canRight and z[a][b+1] == value:
        right = findNumberConnected(a,b+1,z)
    
    return up + left + right + down + 1;

z = [
        [ 0, 0, 0, 1],
        [ 1, 0, 0, 1],
        [ 1, 0, 1, 1],
        [ 1, 0, 0, 1]
    ]
x = len(z)
y = len(z[0])

max = 0

for i in range(x):
    for j in range(y):
        if z[i][j] == 1:
            temp =  findNumberConnected(i,j,z)
            if temp > max:
                max= temp

print (max)
