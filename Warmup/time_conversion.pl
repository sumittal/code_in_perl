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

__DATA__
Problem Statement

You are given time in AM/PM format. Convert this into a 24 hour format.

Note Midnight is 12:00:00AM or 00:00:00 and 12 Noon is 12:00:00PM.

Input Format

Input consists of time in the AM/PM format i.e. hh:mm:ssAM or hh:mm:ssPM 
where 
01≤hh≤12 
00≤mm≤59 
00≤ss≤59

Output Format

You need to print the time in 24 hour format i.e. hh:mm:ss 
where 
00≤hh≤23 
00≤mm≤59 
00≤ss≤59

Sample Input

07:05:45PM
Sample Output

19:05:45
