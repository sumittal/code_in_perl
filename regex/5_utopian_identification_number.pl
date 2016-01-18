use v5.14;
use warnings;

my $n = <> + 0;

foreach ( 1 .. $n) {
    my $line = <>;
    chomp($line);

    if($line =~ /^[a-z]{0,3}[0-9]{2,8}[A-Z]{3,}$/) {
        say "VALID";
    } else {
        say "INVALID";
    }
}
