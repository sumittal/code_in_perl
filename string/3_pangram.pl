use v5.14;
use warnings;

my $line = <>;
chomp($line);
is_pangram($line) ? say 'pangram' : say 'not pangram';

sub is_pangram {
    my $string = shift;

    my $bitset;
    return 0 if (length($string) < 26);

    my @str = split(//,$string);
    foreach my $c (@str) {
        if (ord($c) >= ord('a') && ord($c) <= ord('z')) {
            $bitset |= (1 << (ord($c) - ord('a')));
        } elsif(ord($c) >= ord('A') && ord($c) <= ord('Z')) {
            $bitset |= (1 << (ord($c) - ord('A')));
        }
    } 
    return $bitset == 0x3ffffff;
}
