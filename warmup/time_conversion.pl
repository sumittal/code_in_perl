#Given a time in AM/PM format, convert it to military (2424-hour) time.

#Note: Midnight is 12:00:0012:00:00 AM on a 1212-hour clock and 00:00:0000:00:00 on a 2424-hour clock. Noon is 12:00:0012:00:00 PM on a 1212-hour clock and 12:00:0012:00:00 on a 2424-hour clock.

#Input Format

#A time in 12-hour clock format (i.e.: hh:mm:ssAM or hh:mm:ssPM), where 01≤hh≤1201≤hh≤12.

#Sample Input

#Convert and print the given time in 2424-hour format, where 00≤hh≤2300≤hh≤23.
#07:05:45PM
use v5.14;
use warnings;

my $time = <>;
chomp $time;

my @arr = split( /:/, $time );

my $hh = $arr[0];
my $mm = $arr[1];
my ( $ss, $ff );
if ( $arr[2] =~ /^(\d{2})(\w+)/ ) {
    $ss = $1;
    $ff = $2;
}

if ( ( $ff =~ /^pm$/i ) && ( $hh < 12 ) ) {
    $hh += 12;
}
elsif ( ( $ff =~ /^am$/i ) && ( $hh == 12 ) ) {
    $hh -= 12;
}

$hh = '0' . $hh if ( $hh < 10  && length($hh) == 1 );
say $hh . ':' . $mm . ':' . $ss;
