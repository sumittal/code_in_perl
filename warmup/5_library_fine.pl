use v5.14;
use warnings;

use Date::Calc qw/Delta_Days/;

my $fdate = <>;
chomp($fdate);
my $sdate = <>;
chomp($sdate);

my $fine;
my $diff;

my ( $d1, $m1, $y1 ) = split( / /, $fdate );
my ( $d2, $m2, $y2 ) = split( / /, $sdate );

my @f1 = ( $y1, $m1, $d1 );
my @f2 = ( $y2, $m2, $d2 );

if ( ( $d1 <= $d2 ) && ( $m1 <= $m2 ) && ( $y1 <= $y2 ) ) {
    $fine = 0;
}
elsif ( ( $d1 > $d2 ) && ( $y1 == $y2 ) && ( $m1 == $m2 ) ) {
    $fine = 15 * ( $d1 - $d2 );
}
elsif ( ( $m1 > $m2 ) && ( $y1 == $y2 ) ) {
    $diff = Delta_Days( @f2, @f1 );
    $fine = 500 * ( $m1 - $m2 );
}
elsif ( $y1 > $y2 ) {
    $diff = Delta_Days( @f2, @f1 );
    $fine = 10000 * ( $y1 - $y2 );
}

say $fine;
