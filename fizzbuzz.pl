use strict;
use warnings;

use v5.14;

my $n = <> + 0;

foreach ( 1 .. $n ) {
    my $fizz = ($_ % 3 == 0) ? "Fizz" : "";
    my $buzz = ($_ % 5 == 0) ? "Buzz" : "";
    ($fizz ne "" || $buzz ne "") ? say "$fizz$buzz" : say "$_";
}
