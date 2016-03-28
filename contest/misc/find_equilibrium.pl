#Equilibrium index of an array is an index such that the sum of elements at lower indexes is equal to the sum of elements at higher indexes. For example, in an arrya A:

#A[0] = -7, A[1] = 1, A[2] = 5, A[3] = 2, A[4] = -4, A[5] = 3, A[6]=0

#3 is an equilibrium index, because:
#A[0] + A[1] + A[2] = A[4] + A[5] + A[6]


use strict;
use warnings;

my @in = qw(1 1 1 1 1 1 1 1 8);

print "break point = " . sum_point(@in) . "\n";

sub sum_point {
    my @arr = @_;

	for ( my $i = 0; $i <= scalar(@arr) ; $i++) {
      
      my ($sum1, $sum2);	  
	  # get the sum of first half
	  for ( my $j = 0; $j <= $i ; $j++) {
		$sum1 += $arr[$j];
	  }

	  # get the sum of second half
	  for ( my $j = $i + 1; $j < scalar(@arr) ; $j++) {
          $sum2 += $arr[$j];
	  }

	  if ($sum1 == $sum2) {
		return $i + 1;
	  }
	}
    # if there is no such point
    return -1;
}

#OR
#1) Initialize leftsum  as 0
#2) Get the total sum of the array as sum
#3) Iterate through the array and for each index i, do following.
#    a)  Update sum to get the right sum.  
#        sum = sum - arr[i] 
#        // sum is now right sum
#    b) If leftsum is equal to sum, then return current index. 
#    c) leftsum = leftsum + arr[i] // update leftsum for next iteration.
#    d) return -1 // If we come out of loop without returning then
#        // there is no equilibrium index
