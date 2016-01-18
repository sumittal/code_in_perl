# Enter your code here. Read input from STDIN. Print output to STDOUT
use strict;
use warnings;
use v5.14;

my $in = <>;
chomp($in);

my @in = split(/ /,$in);

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
# Below error contains all possible combination of 4,5,6 for single and double digit
my @fixed = qw(4 5 6 45 54 56 65 46 64);

push @final,@fixed;

for (my $i = 1; $i <= $in[0]; $i++) {
    for (my $j = 1; $j <= $in[1]; $j++) {
         for (my $k = 1; $k <= $in[2]; $k++) {
             my $x = 4 x $i;
             my $y = 5 x $j;
             my $z = 6 x $k;
             
             my @t1 = split(//,$x);
             my @t2 = split(//,$y);
             my @t3 = split(//,$z);
             
             my @arr;
             push @arr,@t1;
             push @arr,@t2;
             push @arr,@t3;
             
             say "@arr";
             permute { push(@final,join('',@_)) } @arr;
         }
    }
}

say "@final";
print 'size -' . @final . "\n";
my %seen;
grep !$seen{$_}++, @final;

my @new_final = keys(%seen);

print 'size -' . @new_final . "\n";
my $sum = 0;
foreach my $i(@new_final) {
    $sum += $i;
}
say $sum;

