use strict;
use Data::Dumper;
use v5.14;

my @users = ( 'Luis', 'Hector', 'Selena', 'Emmanuel', 'Amish' );
my @sorted;
my $first = shift @users;
my $total =
  int( ( $#users / 2 ) * ( $#users + 1 ) );
# to track the index by summing all the index and substracting it from the used index

push @sorted, $first;
my $cnt  = 0;
my $last = lc( chop($first) );

for ( my $i = 0 ; $i <= $#users ; $i++ ) {

    for ( my $j = 0 ; $j <= $#users ; $j++ ) {
        if ( $last eq ( lc( substr( $users[$j], 0, 1 ) ) ) ) {
            $cnt = $cnt + $j;
            my $tmp = $users[$j];
            push( @sorted, $users[$j] );
            $last = lc chop($tmp);
        }
    }
}

my $index = $total - $cnt;
unshift( @sorted, $users[$index] );
print Dumper(@sorted);
~                                                                    
