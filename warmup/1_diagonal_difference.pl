my $t = <>;
my $diff = 0;
my ($s1,$s2);
my $j = 0;
my $i = 0;

LABEL:
for( ;$i<$t; $i++)
{
    $lis = <>;
    @ll = split(' ', $lis);
    for(; $j<$t; $j++) {
        $s1 += $ll[$j];
        $s2 += $ll[$t-$j-1];
        $i++, $j++;
        goto LABEL;
    }
}

$diff = $s1 - $s2;

my $d = ( $diff > 0 ) ? $diff : -($diff);
print $d ."\n";
