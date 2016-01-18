use v5.14;
use warnings;

my $n = <> + 0;

foreach ( 1 .. $n) {
    my $line = <>;
    chomp($line);

    if($line =~ /\b([0-9]{1,3})[\-\s]([0-9]{1,3})[\-\s]([0-9]{4,10})\b/) {
        say "CountryCode=$1,LocalAreaCode=$2,Number=$3";
    }
}
