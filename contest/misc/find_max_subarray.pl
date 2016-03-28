use strict;
use warnings;

sub maxSubArraySum {
    my @in = @_;

	my $max_so_far = 0; 
	my $max_ending_here = 0;
	my $size = scalar(@in);

	for( my $i=0; $i<$size; $i++ ) {
		$max_ending_here = $max_ending_here + $in[$i];
		$max_ending_here = 0 if ($max_ending_here < 0);

		$max_so_far = $max_ending_here if($max_ending_here > $max_so_far);
	}
	return $max_so_far;
}

my @arr = (-2, -3, 4, -1, -2, 1, 5, -3);
print "Maximum contiguous sum is - " . maxSubArraySum(@arr) . "\n";
