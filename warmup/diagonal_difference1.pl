use v5.14;
use warnings;

my $n = <STDIN> + 0;
my ($a, $b) = (0, $n-1);
my ($da, $db) = (0, 0);


while (<STDIN>) {
    last unless $n--;
    my @row = split /\s+/;
    
    $da += $row[$a++];
    $db += $row[$b--];

}
say abs($da - $db);

