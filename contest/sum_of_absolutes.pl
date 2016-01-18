use v5.14;

use strict;
use warnings;

my $f = <>;
chomp($f);
my ($N, $Q) = split(/ /,$f);

my $a = <>;
chomp($a);

my @arr = split(/ /,$a);
die if(scalar(@arr) != $N);

foreach ( 1..$Q ){
    my $line = <>;
    chomp($line);
    my ($l, $r) = split(/ /,$line);
    my $return = find($l, $r);
    if( $return % 2 == 0 ) {
        say "Even";
    } else {
        say "Odd";
    }
}

sub find {
    my ($l,$r) = @_;
    my $sum = 0;
    for(my $i = ($l - 1); $i <= ($r - 1); $i++) {
        $sum = abs($sum + $arr[$i]);
    }
    return $sum;
}
