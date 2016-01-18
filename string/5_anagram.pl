use v5.14;
use warnings;

my $n = <> + 0;

foreach  (1 .. $n) {
    my $line = <>;
    chomp($line);

    say count_replace($line);
}

sub count_replace {
    my $string = shift;

    my $count = 0;
    my $len = length($string);

    # handle if the length of string is odd
    return '-1' if($len % 2 != 0);

    my $first = substr $string, 0, $len/2;
    my $second = substr $string, $len/2, $len;

    my $map1 = buildmap($first);
    my $map2 = buildmap($second);
 
    my @m1 = keys %$map1;
    my @m2 = keys %$map2; 

    foreach my $key (@m2) {
        if( grep(!/$key/, @m1) ) {
            $count += $map2->{$key};
        } else {
            $count += max(0, ($map2->{$key} - $map1->{$key}));
        }
    }
    return $count;
}

sub buildmap {
    my $str = shift;
    my %map;

    my @temp = split(//,$str);
    my @arr = keys %map;

    foreach my $i(0 .. $#temp) {

        if( grep (!/$temp[$i]/, @arr) ) {
            $map{$temp[$i]} = 1;
        } else {
            $map{$temp[$i]} += 1;
        }
    }
   
    return \%map;
}    

sub max {
    my ($a,$b) = @_;

    if($a > $b) {
        return $a;
    } elsif($b > $a) {
        return $b;
    } else {
        return $a;
    }
}
