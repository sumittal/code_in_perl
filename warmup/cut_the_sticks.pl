# You are given NN sticks, where the length of each stick is a positive integer. A cut operation is performed on the sticks such that all of them are reduced by the length of the smallest stick.
#
# Suppose we have six sticks of the following lengths:
# 5 4 4 2 2 8
#
# Then, in one cut operation we make a cut of length 2 from each of the six sticks. For the next cut operation four sticks are left (of non-zero length), whose lengths are the following: 
# 3 2 2 6
#
# The above step is repeated until no sticks are left.
#
# Given the length of NN sticks, print the number of sticks that are left before each subsequent cut operations.
#
# Note: For each cut operation, you have to recalcuate the length of smallest sticks (excluding zero-length sticks).
#
# Input Format 
# The first line contains a single integer NN. 
# The next line contains NN integers: a0, a1,...aN-1 separated by space, where ai represents the length of ith stick.
#
# Output Format 
# For each operation, print the number of sticks that are cut, on separate lines.
#
# Constraints 
# 1 ≤ N ≤ 1000 
# 1 ≤ ai ≤ 1000
#
# Sample Input #00
# 6
# 5 4 4 2 2 8
#
# Sample Output #00
# 6
# 4
# 2
# 1
#
# Sample Input #01
#
# 8
# 1 2 3 4 3 3 2 1
#
# Sample Output #01
#
# 8
# 6
# 4
# 1

#!/usr/bin/perl

$n = <STDIN>;
chomp $n;
$arr_temp = <STDIN>;
@arr = split / /, $arr_temp;
chomp @arr;

computeSticks(@arr);

# With each step, remove all elements from the list that have the same value and print the size of the remaining list.
sub computeSticks {
    my @in = @_;

    my @sorted = sort { $b <=> $a } @in;

    while ( @sorted > 0 ) {
        print @sorted . "\n";

        my $block_cut = pop(@sorted);
        while ( @sorted > 0 && $sorted[-1] <= $block_cut ) {
            pop @sorted;
        }
    }
}

