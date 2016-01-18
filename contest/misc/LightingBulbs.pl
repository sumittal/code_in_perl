use strict;
use warnings;

use Math::Complex;
# This problem can be reduced to finding the numbers that have odd
# number of factors between 1 and itself, and 1, 4, 9, 16, 25, 36, 49, 64,
# 81 and 100 has this property. 
# Enter your code here. Read input from STDIN. Print output to STDOUT

my @input;

while ( my $input = <STDIN> ) {
    chomp($input);
    next if ( $input == 0 );
    if( $input >= 1000000000 || $input < 1) {
        die "The input is out of range\n";
    }
    last unless $input;
    push @input, $input;
}

my $size_of_input = $#input;

my $number_of_tests = shift @input;
if( $number_of_tests >= 10000 || $number_of_tests < 1) {
    die "Wrong number of test cases\n";
}
print "$number_of_tests, $size_of_input\n";

if($number_of_tests != $size_of_input) {
    die "Number of test cases are not equal to number of inputs\n"
}

foreach my $bulb_count (@input) {
    my $on_bulbs = 0;

    foreach my $n ( 1 .. $bulb_count ) {
        $on_bulbs++ if ( is_sqrt( sqrt($n) ) );
    }

    if ( $on_bulbs > 0 ) {
        print $on_bulbs . "\n";
    }

}

sub is_sqrt {
    my $num = shift;

    my $n = $num - int($num);
    my $r = ( $n > 0 ) ? 0 : 1;

    return $r;

}

