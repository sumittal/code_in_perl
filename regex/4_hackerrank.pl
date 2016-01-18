use v5.14;
use warnings;

my $n = <> + 0;

foreach ( 1 .. $n) {
    my $line = <>;
    chomp($line);

    if($line =~ /^hackerrank$/) {
       say "0";
    } elsif($line =~ /^hackerrank/) {
        say "1";
    } elsif($line =~ /hackerrank$/) {
        say "2";
    } else {
        say "-1";
    }
}
