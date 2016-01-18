use v5.14;
use warnings;

my $n = <> + 0;

foreach ( 1 .. $n) {
    my $line = <>;
    chomp($line);

    if($line =~ /^[_\.][0-9]+[a-zA-Z]*_?$/){
        say "VALID";
    } else {
        say "INVALID";
    }
}
