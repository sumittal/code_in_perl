use strict;
use warnings;
use v5.14;

my $in = <>;
chomp($in);

my @in = split(/ /,$in);

my $a = 4 x $in[0];
my $b = 5 x $in[1];
my $c = 6 x $in[2];


my @t1 = split(//,$a);
my @t2 = split(//,$b);
my @t3 = split(//,$c);

my @arr;
push @arr,@t1;
push @arr,@t2;
push @arr,@t3;

say "@arr";

sub permute (&@) {
    my $code = shift;
    my @idx  = 0 .. $#_;
    while ( $code->( @_[@idx] ) ) {
        my $p = $#idx;
        --$p while $idx[ $p - 1 ] > $idx[$p];
        my $q = $p or return;
        push @idx, reverse splice @idx, $p;
        ++$q while $idx[ $p - 1 ] > $idx[$q];
        @idx[ $p - 1, $q ] = @idx[ $q, $p - 1 ];
    }
}

my @final = ();
my @fixed = qw(4 5 6 45 54 56 65 46 64);
push @final,@fixed;

permute { push @final,join('',@_) } @arr;

say "@final";
my $sum = 0;
foreach my $i(@final) {
    $sum += $i;
}
say $sum;
