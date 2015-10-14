print "Type a decimal no - ";
$number = <STDIN>;
chomp $number;

my $hex = '';
my @arr = ( 0 .. 9, 'A' .. 'F' );

while ($number) {
    my $this_digit = $arr[ $number & 15 ];
    $number = int( $number / 16 );
    $hex    = $this_digit . $hex;
}

print "The hexdecimal eqivalent is: $hex\n";
