use strict;
use warnings;

use feature 'say';

my @list;

my $N = <> + 0;
foreach ( 1 .. $N ) {
    my $info = <>;
    chomp($info);

    my $hotel;
    my @words = split( /\s+/, $info );
    $hotel->{Id}       = shift @words;
    $hotel->{price}    = shift @words;
    $hotel->{facility} = \@words;
    push @list, $hotel;

}

my $M = <> + 0;
foreach ( 1 .. $M ) {
    my $test = <>;
    chomp($test);

    my @facilities = split( /\s+/, $test );
    my $budget = shift @facilities;

    my $hotels = get_hotels( $budget, \@facilities );

    say "@$hotels";
}

sub get_hotels {
    my ( $budget, $facilities ) = @_;

    my %id;
    foreach my $value (@list) {

        if ( $budget >= $value->{price} ) {
            my $flag = 1;
            foreach my $x (@$facilities) {

                my @t = split(//,$x);
                next if(@t > 30);
                unless ( grep( /\b$x\b/, @{ $value->{facility} } ) ) {
                    $flag = 0;
                }
            }
            $id{ $value->{Id} } = @{ $value->{facility} } if ($flag);
        }
    }
    my @temp;
    foreach my $val ( sort { $id{$b} <=> $id{$a} } keys %id ) {
        push @temp, $val;
    }
    return \@temp;
}
