# The Utopian Tree goes through 2 cycles of growth every year. Each spring, it doubles in height. Each summer, its height increases by 1 meter.
#
# Laura plants a Utopian Tree sapling with a height of 1 meter at the onset of spring. How tall will her tree be after NN growth cycles?
#
# Input Format
#
# The first line contains an integer, TT, the number of test cases. 
# TT subsequent lines each contain an integer, NN, denoting the number of cycles for that test case.
#
# Constraints 
# 1≤T≤101≤T≤10 
# 0≤N≤600≤N≤60
# Output Format
#
# For each test case, print the height of the Utopian Tree after NN cycles. Each height must be printed on a new line.
# Sample Input
# 3
# 0
# 1
# 4
#
# Sample Output
# 1
# 2
# 7

#!/usr/bin/perl

$t = <STDIN>;
chomp $t;
for my $a0 ( 0 .. $t - 1 ) {
    $n = <STDIN>;
    chomp $n;
    print calculate_height($n) . "\n";
}

sub calculate_height {
    my $in = shift;

    my $h = 1;
    return $h if ( $in == 0 );

    while ($in > 0) {
        if ( $in > 0 ) {
            $h *= 2;
			$in--;
        }
        if ( $in > 0 ) {
            $h++;
			$in--;
        }
    }
    return $h;
}
