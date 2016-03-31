# This is a simple challenge to get things started. Given a sorted array (arar) and a number (VV), can you print the index location of VV in the array?
#
# The next section describes the input format. You can often skip it, if you are using included methods.
#
# Input Format 
# There will be three lines of input:
#
# VV - the value that has to be searched.
# nn - the size of the array.
# arar - nn numbers that make up the array.
# Output Format 
# Output the index of VV in the array.
#
# The next section describes the constraints and ranges of the input. You should check this section to know the range of the input.
#
# Constraints
#
# 1≤n≤10001≤n≤1000
# −1000≤V≤1000,V∈ar−1000≤V≤1000,V∈ar
# It is guaranteed that VV will occur in arar exactly once.
# This "sample" shows the first input test case. It is often useful to go through the sample to understand a challenge.
#
# Sample Input
#
# 4
# 6
# 1 4 5 7 9 12
# Sample Output
#
# 1

use strict;
use warnings;

my $V  = <> + 0;
my $n  = <> + 0;
my $in = <>;
chomp($in);
my @arr = split( /\s+/, $in );

die "wrong size of the array\n" if ( @arr != $n );

my @sorted = sort { $a <=> $b } @arr;

my $low       = 0;
my $high      = $#arr;
my $found_key = 0;
my ( $mid, $index );

while ( $low <= $high && !$found_key ) {

    $mid = int( ( $low + $high ) / 2 );

    if ( $V == $sorted[$mid] ) {
        $found_key = 1;
        $index     = $mid;
    }
    elsif ( $V < $sorted[$mid] ) {
        $high = $mid - 1;
    }
    else {
        $low = $mid + 1;
    }
}

if ($found_key) {
    print $index;
}
else {
    print "Sorry. I could not find: $V";
}

