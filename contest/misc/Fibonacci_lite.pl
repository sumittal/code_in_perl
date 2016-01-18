use strict;
use warnings;

use v5.14;

my $n = <> + 0;
my @num;

sub fab {
  my $a = 0;
  my $b = 1; 
  my $sum;
 
  $n = $_[0];
 
  for (my $i=0;$i<=$n;$i++){
    push @num, $a;
    $sum = $a + $b;
    $a = $b;
    $b = $sum;
  }   
}

fab($n);

say $num[$n];
