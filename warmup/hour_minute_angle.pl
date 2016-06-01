use strict;
use warnings;

print "enter the time in HH:MM format - ";
my $time  = <STDIN>;
chomp($time);

# minute handle rotate 6 degree in 1 minute
# hour hand rotate 1/2 degree in 1 minute
# 
# we will calculate the difference of angle made by hour and minute hand from 12:00

print "Angle between hour and minute hand - " . calculate_angle($time) . "\n";

sub calculate_angle {
	my $time = shift;

	my ($h, $m) = split(':', $time);

	print "invalid format of input\n" if ($h < 0 || $m < 0 || $h > 12 || $m > 60);

    # handle the format where hour can be 1 to 24
    $h = $h % 12;
    
	$h = 0 if($h == 12);
	$m = 0 if($m == 60);

    my $angle_by_hour = 0.5 * ( $h * 60 + $m);
    my $angle_by_minute = 6 * $m;

    my $diff = abs ($angle_by_hour - $angle_by_minute);

    if ($diff > 180) {
    	$diff = 360 - $diff;
    }

    return $diff;

}


