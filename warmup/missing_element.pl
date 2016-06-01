# Print missing elements that lie in range 0 – 99
# Given an array of integers print the missing elements that lie in range 0-99. If there are more than one missing, collate them, otherwise just print the number.
#
# Note that the input array may not be sorted and may contain numbers outside the range [0-99], but only this range is to be considered for printing missing elements.
#
# Examples
#
# Input: {88, 105, 3, 2, 200, 0, 10}
# Output: 1
#         4-9
#         11-87
#         89-99
# Input: {9, 6, 900, 850, 5, 90, 100, 99}
# Output: 0-4
#         7-8
#         10-89
#         91-98
# Expected time complexity O(n), where n is the size of the input array.

use strict;
use warnings;

sub print_missing {
    my @arr = @_;

    my @seen;
    my $LIMIT = 99;

    # Initialize all number from 0 to 99 as NOT seen
    for ( my $i = 0 ; $i < $LIMIT ; $i++ ) {
        $seen[$i] = 0;
    }

    # Mark present elements in range [0-99] as seen
    for ( my $i = 0 ; $i < @arr ; $i++ ) {
        if ( $arr[$i] < $LIMIT ) {
            $seen[ $arr[$i] ] = 1;
        }
    }

    # print missing element
    my $i = 0;
    while ( $i < $LIMIT ) {
        if ( $seen[$i] == 0 ) {

            # Find if there are more missing elements after i
            my $j = $i + 1;
            while ( $j < $LIMIT && $seen[$j] == 0 ) {
                $j++;
            }

            # Print missing single or range
			my $k = $j - 1;
            ( $i + 1 == $j ) ? print "$i\n" : print "$i" . '-' . "$k\n";

            # update i
            $i = $j;
        } else {
            $i++;
        }
    }
}

print "enter the array : ";
my $in = <>;
chomp($in);

my @arr = split(/\s+/, $in);

print_missing(@arr);

