use v5.14;
use warnings;

my $str1 = <>;
my $str2 = <>;

chomp($str1);
chomp($str2);

say anagram($str1,$str2);

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

sub anagram {
    my $s1 = shift;
    my $s2 = shift;

    my $map1 = buildmap($s1);
    my $map2 = buildmap($s2);

    my $count = 0;

    my @m1 = keys %$map1;
    my @m2 = keys %$map2;

    foreach my $key (@m2) {
        if( grep(!/$key/, @m1) ) {
            $count += $map2->{$key};
        } else {
            $count += max(0, ($map2->{$key} - $map1->{$key}));
        }
    }

    foreach my $key (@m1) {
        if( grep(!/$key/, @m2) ) {
            $count += $map1->{$key};
        } else {
            $count += max(0, ($map1->{$key} - $map2->{$key}));
        }

    return $count;
    }
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
