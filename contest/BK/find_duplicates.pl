use strict;
use warnings;

use v5.14;

my @in = (1, 1, 2, 3, 2);

printRepeating(\@in);

sub printRepeating {
    my $var = shift;

    my @arr = @$var;

    for(my $i = 0; $i <= $#arr; $i++) {
        if($arr[abs($arr[$i])] > 0) {
            $arr[abs($arr[$i])] = -$arr[abs($arr[$i])];
        } else {
            say abs($arr[$i]);
        }
    }
}
