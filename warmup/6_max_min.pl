use v5.14;
use warnings;

use Data::Dumper;

my $n = <> + 0;
my $k = <> + 0;
my @arr;

foreach(0 .. $n-1) {
    my $i = <> + 0;
    push @arr,$i;
}


sub get_unfairness {
    my ($n,$k,$arr) = @_;
    my $t;

    my @sorted_arr = sort {$a <=> $b} @$arr;
    $k = $k -1;

    foreach my $x (0..$n-1) {
        if($x + $k < $n){
            my $temp = $sorted_arr[$x + $k] - $sorted_arr[$x];

            $t->{$temp} = [@sorted_arr[$x .. ($x + $k)]];
#            printf ("N:%d k:%d x:%d\n",$n,$k,$x);
        }
    }

#    print Dumper($t);
    foreach my $key ( sort { $a <=> $b } keys %$t ) {
       # print "$key - @{$t->{ $key }}" . "\n";
        return $key;
    }
}


my $diff = get_unfairness($n,$k,\@arr);
say $diff;
