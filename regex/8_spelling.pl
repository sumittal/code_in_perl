use v5.14;
use warnings;

my $n = <> + 0;
my @out;

foreach ( 1 .. $n) {
    my $line = <>;
    chomp($line);

    if( $line =~ /\b(\w+(?:(?:ze)|(?:se)))\b/ ) {
        push @out, $1;
    }
}

say scalar(@out);
