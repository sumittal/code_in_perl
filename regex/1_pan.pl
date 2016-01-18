use v5.14;
use warnings;

my $n = <> + 0;

foreach ( 1 .. $n) {
    my $line = <>;
    chomp($line);

    if(length($line) == 10) {
        if($line =~ /\b[A-Z]{5}[0-9]{4}[A-Z]{1}\b/) {
            say "YES";
        } else {
             say "NO";
        }
    }
}
