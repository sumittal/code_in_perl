use v5.14;
use warnings;

my $n = <> + 0;
my $count = 0;

foreach ( 1 .. $n) {
    my $line = <>;
    chomp($line);

    if($line =~ /hackerrank/i) {
        $count++;
    }
}
say $count;
