use v5.14;
use warnings;

my $n = <> + 0;

foreach  (1 .. $n) {
    my $line = <>;
    chomp($line);

    count_delete($line);
}

sub count_delete {
    my $string = shift;

    my @str = split(//,$string);
    my $count = 0;
    foreach my $i(1 .. $#str) {
        if($str[$i] eq $str[$i-1]) {
            $count++;
        }
    }
    say $count;
}
