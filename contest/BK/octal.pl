print "Type a decimal no - ";
$number = <STDIN>;
chomp $number;

my $oct = '';

while ($number) {
    my @arr = ( 0 .. 7 );
    my $this_digit = $arr[ $number & 7 ];
    $number = int( $number / 8 );
    $oct = $this_digit . $oct;
}

print "The octal equivalent is : $oct\n";
