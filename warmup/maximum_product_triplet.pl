# Given an integer array, find a maximum product of a triplet in array.
#
# Examples:
#
# Input:  [10, 3, 5, 6, 20]
# Output: 1200
# Multiplication of 10, 6 and 20
#  
#  Input:  [-10, -3, -5, -6, -20]
#  Output: -90
#
#  Input:  [1, -4, 3, -6, 7, 0]
#  Output: 168
use strict;
use warnings;

my @in = qw(1 -4 3 -6 7 0);

my $max = maxProduct(@in);

if ( $max == -1 ) {
    print "No Triplet Exists\n";
} else {
    print "Maximum product is $max\n";
}

sub maxProduct {
    my @arr = @_;

    my $n = scalar(@arr);

    # if size is less than 3, no triplet exists
    return -1 if ( $n < 3 );

    # Initialize Maximum, second maximum and third
    # maximum element
    my ( $maxA, $maxB, $maxC ) =
      ( -999_999_999_99, -999_999_999_99, -999_999_999_99 );

    # Initialize Minimum and second mimimum element
    my ( $minA, $minB ) = ( 999_999_999_99, 999_999_999_99 );

    for ( my $i = 0 ; $i < $n ; $i++ ) {

        # Update Maximum, second maximum and third
        # maximum element

        if ( $arr[$i] > $maxA ) {
            $maxC = $maxB;
            $maxB = $maxC;
            $maxA = $arr[$i];

            # Update second maximum and third maximum element
        } elsif ( $arr[$i] > $maxB ) {
            $maxC = $maxB;
            $maxB = $arr[$i];

            # Update third maximum element
        } elsif ( $arr[$i] > $maxC ) {
            $maxC = $arr[$i];
        }

        # Update Minimum and second mimimum element
        if ( $arr[$i] < $minA ) {
            $minB = $minA;
            $minA = $arr[$i];
        } elsif ( $arr[$i] < $minB ) {
            $minB = $arr[$i];
        }

    }
    return max( $minA * $minB * $maxA, $maxA * $maxB * $maxC );
}

sub max {
    my ( $a, $b ) = @_;

    $a > $b ? return $a : return $b;
}

