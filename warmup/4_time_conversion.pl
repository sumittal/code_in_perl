# Enter your code here. Read input from STDIN. Print output to STDOUT
use v5.14;
use warnings;

my $input = <>;

my @arr = split(/:/,$input);

my $hh = $arr[0];
my $mm = $arr[1];
my ($ss, $ff);

if( $arr[2] =~ /^(\d{2})(\w+)/ ) {
    $ss = $1;
    $ff = $2;
}

print "$hh $mm $ss\n";

if(($ff =~ /^pm$/i) && ($hh < 12) ) {
    $hh += 12;
} elsif( ($ff =~ /^am$/i) && ($hh == 12) ) {
    $hh -= 12;
}

$hh = '0' . $hh if($hh < 10);
say $hh . ':' . $mm . ':' . $ss;

