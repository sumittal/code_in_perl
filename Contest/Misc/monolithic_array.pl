#Create monolithic sublists from an array of integers ,in increasing order for example [1,2,4,7,5,6,3,2] will give [[1,2,4,7][5,6],[3],[2]]

use strict;
use warnings;
use v5.14;

use Data::Dumper;

my @array = ( 1, 2, 4, 7, 5, 6, 3, 2 );
my @sub;
my $i = 0;

while ( $i <= $#array ) {
    my @set;
    push( @set, $array[$i] );
    for ( my $j = $i ; $j <= $#array - 1 ; $j++ ) {
        if ( $array[$j] <= $array[ $j + 1 ] ) {
            push( @set, $array[ $j + 1 ] );
        }
        else {
            $i = $j + 1;
            last;
        }
    }
    push( @sub, \@set );
}

say Dumper(\@sub);
