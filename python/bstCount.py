"""
The number of binary search trees can be seen as a recursive solution. i.e., 
Number of binary search trees = (Number of Left binary search sub-trees) * (Number of Right binary search sub-trees) * (Ways to choose the root)

In a BST, only the relative ordering between the elements matter. So, without any loss on generality, we can assume the 
distinct elements in the tree are 1, 2, 3, 4, ...., n. Also, let the number of BST be represented by f(n) for n elements.

Now we have the multiple cases for choosing the root.

choose 1 as root, no element can be inserted on the left sub-tree. n-1 elements will be inserted on the right sub-tree.
Choose 2 as root, 1 element can be inserted on the left sub-tree. n-2 elements can be inserted on the right sub-tree.
Choose 3 as root, 2 element can be inserted on the left sub-tree. n-3 elements can be inserted on the right sub-tree.
...... Similarly, for i-th element as the root, i-1 elements can be on the left and n-i on the right.

"""
def CountBST(nvalues):
 
    result = [] 
    for i in nvalues:
        result.append(catalan(i))
    return result

def countBT(nval):
    result = []
    for n in nval:
        count = catalan(n)
        res =  count * factorial(n)
        result.append(res)
    return result

def factorial(n):
    res = 1;
    for i in xrange(1,n+1):
        res *= i;
    return res;
 
def binomialCoeff(n, k):
    res = 1;
 
    if (k > n - k):
        k = n - k
 
    for i in xrange(k):
        res *= (n - i);
        res /= (i + 1);

    return res;
 
def catalan(n):
    c = binomialCoeff(2*n, n);
 
    return c/(n+1);

print(CountBST([10,39,59,96,2,5,36]))
print(countBT([10,39,59,96,2,5,36]))
print(CountBST([2,3,4,100]))
print(countBT([2,3,4,100]))
