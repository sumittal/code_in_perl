use strict;
use warnings;

use v5.14;

my $str = <>;
chomp($str);
say get_uncoupled_value($str);

sub get_uncoupled_value {
    my $input = shift;

    my @list = split(/,\s+/,$input);
    my $value = 0;

    foreach my $i ( 0 .. $#list ) {
        $value ^= $list[$i];
    }

    return $value;
}
