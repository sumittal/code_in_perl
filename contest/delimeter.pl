use strict;
use warnings;

use v5.14;

my $str = <>;
chomp($str);

my @list = split(//,$str);
my %h;

foreach my $i ( @list ) {
    $h{$i} += 1;
}
}
if( ( $h{'('} == $h{')'} ) && ( $h{'{'} == $h{'}'} ) && ( $h{'['} == $h{']'} ) ) {
    say 'True';
} else {
    say 'False';
}    

