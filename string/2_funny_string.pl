use v5.14;
use warnings;

my $n = <> + 0;

foreach  (1 .. $n) {
    my $line = <>;
    chomp($line);
    
    is_funny($line);
}

sub is_funny {
    my $string = shift;

    my $flag = 0;
    my @str = split(//,$string);
    my @rstr = split(//,reverse($string)); 

    for(my $i = 1; $i <= $#str -1; $i++) {
        my $diff = abs(ord($str[$i]) - ord($str[$i-1]));
        my $rdiff = abs(ord($rstr[$i]) - ord($rstr[$i-1]));

        if( $diff == $rdiff) {
            $flag = 1;
        } else {
           $flag = 0;
           last;
        }
    }
    $flag ? say 'Funny' : say 'Not Funny';
}
