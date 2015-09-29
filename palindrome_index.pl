use v5.14;
use warnings;
use strict;

my $T = <> + 0;

foreach ( 1 .. $T ) {
    my $str = <>;
    chomp($str);
    say pindex($str);
}

sub pindex {
    my $str = shift;
    my @str = split(//,$str);

    return '-1' if($str eq reverse($str));
    my $j = $#str;
    my $i = 0;

    while ( $i < $j ) {

        if( $str[$i] eq $str[$j] ){
            $i++; $j--;
        } elsif($str[$i + 1] eq $str[$j] ) {
            return $i;
            break;
        } elsif($str[$i] eq $str[$j - 1] ) {
           return $j;
           break;
        }
    }
    return '-1' if( $j > $i);
}
