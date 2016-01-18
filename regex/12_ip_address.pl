# Enter your code here. Read input from STDIN. Print output to STDOUT
use v5.14;
use warnings;

my $n = <> + 0;

foreach (1 .. $n) {
    my $line = <>;
    chomp($line);
    if( $line =~ /^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$/ix ) {
        say "IPv4";
    } elsif($line =~ /^(([\da-f]{0,4}:{0,2}){1,8})$/i) {
        say "IPv6";
    } else {
        say "Neither";
    }
}
