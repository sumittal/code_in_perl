my $t = <>;
my $diff = 0;
my ($s1,$s2);
my $j = 0;
my $i = 0;

LABEL:
for( ;$i<$t; $i++)
{
    $lis = <>;
    @ll = split(' ', $lis);
    for(; $j<$t; $j++) {
        $s1 += $ll[$j];
        $s2 += $ll[$t-$j-1];
        $i++, $j++;
        goto LABEL;
    }
}

$diff = $s1 - $s2;

my $d = ( $diff > 0 ) ? $diff : -($diff);
print $d ."\n";

__DATA__
Problem Statement

You are given a square matrix of size N×N. Calculate the absolute difference of the sums across the two main diagonals.

Input Format

The first line contains a single integer N. The next N lines contain the rows of N integers describing the matrix.

Constraints 
1≤N≤100 
−100≤A[i]≤100
Output Format

Output a single integer equal to the absolute difference in the sums across the diagonals.

Sample Input

3
11 2 4
4 5 6
10 8 -12
Sample Output

15
Explanation

The first diagonal of the matrix is:

11
    5
        -12
Sum across the first diagonal: 11 + 5 - 12 = 4

The second diagonal of the matrix is:

        4
    5
10
Sum across the second diagonal: 4 + 5 + 10 = 19 
Difference: |4 - 19| = 15
