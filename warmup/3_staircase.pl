use v5.14;
use warnings;

my $n = <> + 0;
my $i =1;

while($n) {
    my $s = ' ' x ($n - 1);
    $s .= '#' x $i;
    say $s;
    $n--;
    $i++;
}
